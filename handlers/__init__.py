from aiogram import Dispatcher

from . import joystick
from . import commands

def include_routers(dp: Dispatcher):
    """Пудключить все обработчики событий в один диспетчер"""
    dp.include_routers(
        joystick.router,
        commands.router)
