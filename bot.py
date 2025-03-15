import asyncio
from os import getenv

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from bot_menu import set_bot_menu
from handelers.commands import command_router
from handelers.handlers import handlers_router

load_dotenv()
TOKEN = getenv("TOKEN")
    
dp = Dispatcher()

router = Router()



async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(router)
    dp.include_router(command_router)
    dp.include_router(handlers_router)
    await set_bot_menu(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Starting bot...")
    asyncio.run(main())