import asyncio

from database.database import SessionLocal
from . import dp, bot
from .middleware import DatabaseMiddleware


async def bot_start_polling():
    """
    Start the bot polling loop
    (added database middleware if is outside Flask Api server)
    """
    dp.update.middleware(DatabaseMiddleware(SessionLocal))
    await dp.start_polling(bot)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot_start_polling())
