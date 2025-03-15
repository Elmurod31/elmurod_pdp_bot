import os

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

from handelers.keyboards import add_btns

command_router = Router()


@command_router.message(CommandStart())
async def command_start_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_1.png")
    img = FSInputFile(img_path)
    await message.answer_photo(img, caption="Assalomu alaykom PDP Junior botiga hush kelib siz! 😊", reply_markup=add_btns)