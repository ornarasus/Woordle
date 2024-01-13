import asyncio
from lxml import etree
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from os import getenv
from game import Game

attempts = int(getenv("COUNT_ATTEMPTS"))
count = int(getenv("COUNT_LITTERS"))
bot = Bot(getenv("TOKEN"))
tree = etree.parse('words.xml')
root = tree.getroot()
words = []
for p in root.xpath('//word[@count="5"]'):
    words.append(p.get("text"))
dp = Dispatcher()

games: dict[int, Game] = {}

for i in range(len(words)):
    words[i] = words[i].lower()


@dp.message(Command("play"))
async def start_game(msg: Message):
    games[msg.from_user.id] = Game(words)
    await msg.answer("Игра началась!\n"
                     f"Отправьте слово из {count} букв\n\n"
                     "Условные обозначения:\n"
                     "- точно нет в целевом слове\n"
                     "- <u>есть в слове, но не в том месте</u>\n"
                     "- <b>ЕСТЬ В СЛОВЕ, И В ЭТОМ МЕСТЕ</b>",
                     parse_mode="html")


@dp.message()
async def on_message(msg: Message):
    if msg.from_user.id in list(games.keys()):
        if len(msg.text) == count:
            textmsg = msg.text.lower()
            if textmsg in words:
                games[msg.from_user.id].add_attempts(textmsg)
                text = f"Попытки({len(games[msg.from_user.id].attempts)}/{attempts}):"
                for i in range(len(games[msg.from_user.id].attempts)):
                    text += f"\n{i+1}) "
                    for l in games[msg.from_user.id].attempts[i].letters:
                        match l.type:
                            case 0:
                                text += l.text.lower()
                            case 1:
                                text += f"<b>{l.text}</b>".upper()
                            case 2:
                                text += f"<u>{l.text}</u>"
                await msg.answer(text, parse_mode="html")
                if games[msg.from_user.id].is_win:
                    await msg.answer("Загаданое слово было отгадано.")
                elif len(games[msg.from_user.id].attempts) == 6:
                    await msg.answer(
                        f"Попытки закончились\nЗагаданое слово: {games[msg.from_user.id].answer}",
                        parse_mode="html")
                    games.pop(msg.from_user.id)
            else:
                await msg.answer("Вы отправили неизвестное слово!")
        else:
            await msg.answer(f"В слове должно быть {count} букв!")
    else:
        await msg.answer("Чтобы запустить игру напишите /play")


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
