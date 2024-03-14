from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from keyboards.joystick import get_specs

import asyncio

router = Router()

@router.message(Command("start"))
async def bot_start(msg: Message):
    await msg.answer(text="Приветсвую командир, Вам нужно выбрать военную специальность./n Вы можете узнать подробнее о каждой из них отправив команду /specialties", reply_markup=get_specs)
@router.message(Command("specialties"))
async def bot_specs(msg: Message):
    await msg.answer(text="Стрелок - описание возможностей. Диверсант - описание. Гранотометчик - описание")
@router.callback_query(F.data is not None)
async def bot_spec_message(callback: CallbackQuery):
    await callback.message.answer(text=f'Поздравляю, Новый игрок, теперь вы {callback.data}! Ваши координаты координаты и карта местности')