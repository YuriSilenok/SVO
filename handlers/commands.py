from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from models import User, Player
from keyboards.joystick import get_specialties

import asyncio

router = Router()

@router.message(Command("start"))
async def bot_start(msg: Message):
    User.get_or_create(
        tg_id = Message.from_user.id
    )
    await msg.answer(text="Приветсвую командир, Вам нужно выбрать военную специальность."
                     "/n Вы можете узнать подробнее о каждой из них отправив команду /specialties",
                       reply_markup=get_specialties)

@router.message(Command("specialties"))
async def bot_specialties(msg: Message):
    await msg.answer(text="Стрелок - описание возможностей."
                     "Диверсант - описание."
                     "Гранотометчик - описание")

@router.callback_query_handler('specialty')
async def bot_spec_message(callback_query: CallbackQuery):
    player = Player.get_or_create(
        Player.user.tg_id == Message.from_user.id, 
        Player.specialty == callback_query.data,
        Player.x == 100600,
        Player.y == -100600
        )
    await callback_query.message.answer(text=f'Поздравляю, {player.nickname},"
                                        " теперь вы {player.specialty}!"
                                        " Ваши координаты координаты ({player.x},"
                                        "{player.y}) и карта местности')