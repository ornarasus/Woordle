from abc import ABC
from utils import getenv
from lxml import etree

from aiogram import Bot

from entities.game import Game


class Env(ABC):
    words: list[str]
    attempts: int
    count: int
    bot: Bot
    games: dict[int, Game]

    @staticmethod
    def init():
        Env.attempts = int(getenv("COUNT_ATTEMPTS", default="6"))
        Env.count = int(getenv("COUNT_LETTERS", default="5"))
        Env.bot = Bot(getenv("TOKEN", err_msg="Отсутствует токен бота. Его можно получить у @BotFather"))
        root = etree.parse('words.xml', None).getroot()
        Env.words = []
        for p in root.xpath(f'//word[@count="{Env.count}"]'):
            Env.words.append(p.get("text"))
        Env.games = {}
        for i in range(len(Env.words)):
            Env.words[i] = Env.words[i].lower()

