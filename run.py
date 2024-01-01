import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from game import Game
from settings import *

bot = Bot(token)
dp = Dispatcher()

games: dict[int, Game] = {}

for i in range(len(words)):
    words[i] = words[i].lower()


@dp.message(Command("play"))
async def start_game(msg: Message):
    games[msg.from_user.id] = Game()
    await msg.answer("Игра началась!\nОтправьте слово из 5 букв")


@dp.message()
async def on_message(msg: Message):
    if msg.from_user.id in list(games.keys()):
        if len(msg.text) == 5:
            textmsg = msg.text.lower()
            if textmsg in words:

                games[msg.from_user.id].add_attempts(textmsg)
                text = f"Попытки({len(games[msg.from_user.id].attempts)}/{attempts}):"
                for i in range(len(games[msg.from_user.id].attempts)):
                    text += f"\n{i+1}) "
                    for l in games[msg.from_user.id].attempts[i].letters:
                        match l.type:
                            case 0:
                                text += f"{l.text}"
                            case 1:
                                text += f"<b><i>{l.text}</i></b>"
                            case 2:
                                text += f"<u>{l.text}</u>"
                await msg.answer(text, parse_mode="html")
                if games[msg.from_user.id].is_win:
                    await msg.answer(f"Загаданое слово ({games[msg.from_user.id].answer}) было отгадано за {len(games[msg.from_user.id].attempts)} попыток(у/и).")
                elif len(games[msg.from_user.id].attempts) == 6:
                    await msg.answer(
                        f"Попытки закончились\nЗагаданое слово: {games[msg.from_user.id].answer}",
                        parse_mode="html")
                    games.pop(msg.from_user.id)
            else:
                await msg.answer("Вы отправили неизвестное слово!")
        else:
            await msg.answer("В слове должно быть 5 букв!")
    else:
        await msg.answer("Чтобы запустить игру напишите /play")
    ...


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
