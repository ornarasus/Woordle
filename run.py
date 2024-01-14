import asyncio
from routers import RNewGame, RCheck
from aiogram import Dispatcher
from env import Env


async def main():
    Env.init()
    dp = Dispatcher()
    dp.include_routers(RNewGame, RCheck)
    await dp.start_polling(Env.bot)


if __name__ == "__main__":
    asyncio.run(main())
