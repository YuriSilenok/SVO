from aiogram import F, Router

from aiogram.utils.keyboard import InlineKeyboardBuilder
router = Router()
def get_specs():
    kb=InlineKeyboardBuilder()
    kb.button(text="Стрелок", callback_data=0)
    kb.button(text="Минометчик", callback_data=1)
    kb.button(text="Связист", callback_data=2)
    kb.button(text="Инженер", callback_data=3)
    kb.adjust(1)
    return kb.as_markup()
