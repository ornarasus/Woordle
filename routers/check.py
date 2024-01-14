from typing import NoReturn
from aiogram import Router, F
from aiogram.types import Message
from enums.letter_type import LetterType

from env import Env


router = Router()


def show_attempt(uid: int, aid: int) -> str:
    attempt = ""
    for l in Env.games[uid].attempts[aid].letters:
        match l.type:
            case LetterType.WRONG:
                attempt += l.text.lower()
            case LetterType.RIGHT:
                attempt += f"<b>{l.text}</b>".upper()
            case LetterType.OTHER_PLACE:
                attempt += f"<u>{l.text}</u>".lower()
    return attempt


async def check_end(uid: int) -> None:
    if Env.games[uid].is_win:
        await Env.bot.send_message(uid, "Загаданое слово было отгадано.")
    elif len(Env.games[uid].attempts) == Env.attempts:
        await Env.bot.send_message(
            chat_id=uid, parse_mode="html",
            text=f"Попытки закончились\nЗагаданое слово: {Env.games[uid].answer}")
        Env.games.pop(uid)


@router.message(F.text)
async def check(msg: Message):
    if msg.text and msg.from_user:
        if msg.from_user.id in list(Env.games.keys()):
            if len(msg.text) == Env.count:
                textmsg = msg.text.lower()
                if textmsg in Env.words:
                    Env.games[msg.from_user.id].add_attempts(textmsg)
                    text = f"Попытки({len(Env.games[msg.from_user.id].attempts)}/{Env.attempts}):"
                    for i in range(len(Env.games[msg.from_user.id].attempts)):
                        text += f"\n{i+1}) {show_attempt(msg.from_user.id, i)}"                        
                    await msg.answer(text, parse_mode="html")
                    await check_end(msg.from_user.id)
                else:
                    await msg.answer("Вы отправили неизвестное слово!")
            else:
                await msg.answer(f"В слове должно быть {Env.count} букв!")
        else:
            await msg.answer('Чтобы запустить игру, перезапустите бота (/start).')
