import logging
import aiogram
import asyncio
from aiogram import Dispatcher, Bot
from config import TOKEN
from aiogram.filters import CommandStart
from aiogram.types import Message
from funcshional import handlers
dp = Dispatcher()



handlers.reg_handler(dp)
bot = Bot(token=TOKEN)






async def main():
    await dp.start_polling(bot)
    



if __name__ == "__main__":
    
    try:
        asyncio.run(main())
        
    except KeyboardInterrupt:
        print("Stopped")   





