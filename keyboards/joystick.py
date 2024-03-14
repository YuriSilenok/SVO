from aiogram import F, Router

from aiogram.utils.keyboard import InlineKeyboardBuilder
router = Router()
def get_specs():
    kb=InlineKeyboardBuilder()
    kb.button(text="Стрелок", callback_data="Rifler")
    kb.button(text="Минометчик", callback_data="Artillery")
    kb.button(text="Связист", callback_data="Operator")
    kb.button(text="Инженер", callback_data="Engineer")
    kb.adjust(1)
    return kb.as_markup()