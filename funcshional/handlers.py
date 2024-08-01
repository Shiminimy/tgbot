from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.dispatcher import router

from aiogram.filters import Command, CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.methods import EditMessageText
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
dp = Dispatcher()

























async def start(message: Message):
    await message.answer("Hi!")
def reg_handler(dp):
    dp.message.register(start, F.text == '/start')