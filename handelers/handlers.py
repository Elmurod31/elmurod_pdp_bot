import os

from aiogram import Router, F
from aiogram.types import Message, FSInputFile

from handelers.keyboards import adds_btns, add_btns, adds_btnss

handlers_router = Router()


@handlers_router.message(F.text == "Kompaniya haqida")
async def command_start_handler(message: Message):
    img_path_1 = os.path.join(os.path.dirname(__file__), "images", "img.png")
    img = FSInputFile(img_path_1)
    await message.answer_photo(img, caption="8 yillik tajribaga, 2000 mingdan ortiq o'quvchilar va tajribali mentorlar ega! 😊")


@handlers_router.message(F.text == "Bizning mentorlar")
async def command_start_handler(message: Message):
    img_path_2 = os.path.join(os.path.dirname(__file__), "images", "img_2.png")
    img_path_3 = os.path.join(os.path.dirname(__file__), "images", "img_3.png")
    img_path_4 = os.path.join(os.path.dirname(__file__), "images", "img_4.png")
    img_path_5 = os.path.join(os.path.dirname(__file__), "images", "img_5.png")
    img_path_6 = os.path.join(os.path.dirname(__file__), "images", "img_6.png")
    img_path_7 = os.path.join(os.path.dirname(__file__), "images", "img_7.png")
    img_path_8 = os.path.join(os.path.dirname(__file__), "images", "img_8.png")
    images= [[img_path_2, "Mentor: Shohruh Abdurahmon"], [img_path_3, "Mentor: Asilbek Madaliyev"], [img_path_4, "Mentor: Habibulloh Nuriddinov"], [img_path_5, "Mentor: Asadbek Erkinov"], [img_path_6, "Mentor: Baxodir Isroilov"], [img_path_7, "Mentor: Jaxongir Abduraimov"], [img_path_8, "Mentor: Abrorjon Abdusaidov"]]
    for path in images:
        img = FSInputFile(path[0])
        await message.answer_photo(img, caption=path[1])



#start
@handlers_router.message(F.text == "Kurslarimiz")
async def command_start_handler(message: Message):
    await message.answer(text="Bizning kurslarimiz", reply_markup=adds_btns)


@handlers_router.message(F.text == "Kontaktlar/Manzil")
async def command_start_handler(message: Message):
    img_path_1 = os.path.join(os.path.dirname(__file__), "images", "img_13.png")
    img = FSInputFile(img_path_1)
    await message.answer_photo(img, caption=" +998 78 777 74 77\n"
                                            " Toshkent shahri, Shayhontoxur tumani\n"
                                            " Chorsu Xadra, Zarqaynar 3uy! 😊")




#kurslarimiz
@handlers_router.message(F.text == "Python")
async def command_start_handler(message: Message):
    img_path_1 = os.path.join(os.path.dirname(__file__), "images", "img_9.png")
    img = FSInputFile(img_path_1)
    await message.answer_photo(img, caption="Python - Mantiqiy fikirlash va dasturlash asoslari! 😊")


@handlers_router.message(F.text == "Fronted")
async def command_start_handler(message: Message):
    img_path_1 = os.path.join(os.path.dirname(__file__), "images", "img_12.png")
    img = FSInputFile(img_path_1)
    await message.answer_photo(img, caption="Fronted - web dasturlash dastlabki qadamlar! 😊")


@handlers_router.message(F.text == "Robototexnika")
async def command_start_handler(message: Message):
    img_path_1 = os.path.join(os.path.dirname(__file__), "images", "img_10.png")
    img = FSInputFile(img_path_1)
    await message.answer_photo(img, caption="Robototexnika - texnik ko'nikmalar va amaliy ishlar! 😊")


@handlers_router.message(F.text == "Scratch")
async def command_start_handler(message: Message):
    img_path_1 = os.path.join(os.path.dirname(__file__), "images", "img_11.png")
    img = FSInputFile(img_path_1)
    await message.answer_photo(img, caption="Scratch - Vizual dasturlash orqali kreativ fikirlash! 😊")


@handlers_router.message(F.text == "Back")
async def command_start_handler(message: Message):
    await message.answer(text="Kurslarimiz", reply_markup=add_btns)


#til
@handlers_router.message(F.text == "Til")
async def command_start_handler(message: Message):
    await message.answer(text="Til tanlang! 😊", reply_markup=adds_btnss)

@handlers_router.message(F.text == "Uzbek tili")
async def command_start_handler(message: Message):
    await message.answer(text="Til qabul qilindi! 😊")

@handlers_router.message(F.text == "English")
async def command_start_handler(message: Message):
    await message.answer(text="Language selected! 😊")

@handlers_router.message(F.text == "Orqaga")
async def command_start_handler(message: Message):
    await message.answer(text="Orqaga! 😊", reply_markup=add_btns)
