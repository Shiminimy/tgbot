from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder



async def mainBtn():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Dungeons", callback_data='dungeons'))
    builder.add(types.InlineKeyboardButton(text="Dailyk", callback_data='daylik'))
    return builder.as_markup()