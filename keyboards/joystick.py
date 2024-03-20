from aiogram import Router
from models import Specialty

from aiogram.utils import InlineKeyboardBuilder


router = Router()
def get_specialties():
    kb=InlineKeyboardBuilder()
    for i in len(Specialty):
        kb.button(text=Specialty.get_by_id(i), callback_data = 'specialty')
    kb.adjust(1)
    return kb.as_markup()
