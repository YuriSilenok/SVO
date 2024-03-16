import os
import asyncio

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.bot import DefaultBotProperties

import handlers


load_dotenv('.env')
token = os.getenv("TG_TOKEN") or ""
bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


async def main():
    """Запуск основных задач бота"""
    handlers.include_routers(dp)
    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    asyncio.run(main())
