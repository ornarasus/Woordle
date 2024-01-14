from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from entities.game import Game

from env import Env


router = Router()

@router.message(Command("start"))
async def new_game(msg: Message):
    if msg.from_user:
        Env.games[msg.from_user.id] = Game()
        await msg.answer("Игра началась!\n"
                        f"Отправьте слово из {Env.count} букв\n\n"
                        "Условные обозначения:\n"
                        "- точно нет в целевом слове\n"
                        "- <u>есть в слове, но не в том месте</u>\n"
                        "- <b>ЕСТЬ В СЛОВЕ, И В ЭТОМ МЕСТЕ</b>",
                        parse_mode="html")
