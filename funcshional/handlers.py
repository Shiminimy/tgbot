from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.dispatcher import router
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.methods import EditMessageText
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
dp = Dispatcher()
router = Router()
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import funcshional.keyboards as k

class Reg(StatesGroup):
    name = State()
    number = State()


    


async def start(message: Message):
    await message.answer("Hello I am bot, type help to receive a list of available commands")



async def help(message: Message):
    await message.answer(f"Commands:", reply_markup= await k.mainBtn())




async def reg(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer("Type NAme:")



async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer("Type number:")



async def reg_thr(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f'Done, Name: {data["name"]}, Number: {data["number"]}')
    await state.clear()


























def reg_handler(dp):
    #dp.message.register(help, Command("start"))
    dp.message.register(reg, Command("reg"))
    dp.message.register(reg_two, Reg.name)
    dp.message.register(reg_thr, Reg.number)
    #router.message.register(cmd_start, CommandStart())
    dp.include_router(router)