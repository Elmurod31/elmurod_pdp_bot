from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

add_btns = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="Kompaniya haqida"),
        KeyboardButton(text="Bizning mentorlar"),
    ],
    [
        KeyboardButton(text="Kurslarimiz"),
    ],
    [
        KeyboardButton(text="Kontaktlar/Manzil"),
        KeyboardButton(text="Til"),
    ]
], resize_keyboard=True)

adds_btns = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="Python"),
        KeyboardButton(text="Fronted"),
    ],
    [
        KeyboardButton(text="Robototexnika"),
        KeyboardButton(text="Scratch")
    ],
    [
        KeyboardButton(text="Back"),
    ]
], resize_keyboard=True)

adds_btnss = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="Uzbek tili"),
        KeyboardButton(text="English"),
    ],
    [
        KeyboardButton(text="Orqaga"),
    ],
], resize_keyboard=True)