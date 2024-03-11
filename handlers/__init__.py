from aiogram import Dispatcher

from . import joystick
from . import commands

def include_routers(dp: Dispatcher):
    dp.include_routers(
        joystick.router, 
        commands.router)