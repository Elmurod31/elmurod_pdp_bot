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
        KeyboardButton(text="Orqaga"),
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




add_btns1 = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="About the company"),      # Kompaniya haqida
        KeyboardButton(text="Our mentors"),            # Bizning mentorlar
    ],
    [
        KeyboardButton(text="Our courses"),            # Kurslarimiz
    ],
    [
        KeyboardButton(text="Contacts/Address"),       # Kontaktlar/Manzil
        KeyboardButton(text="Language"),               # Til
    ]
], resize_keyboard=True)

adds_btns2 = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="python"),
        KeyboardButton(text="frontend"),               # Fronted -> Frontend (to'g'rilandi)
    ],
    [
        KeyboardButton(text="robotics"),               # Robototexnika
        KeyboardButton(text="scratch")
    ],
    [
        KeyboardButton(text="back"),                   # Back (qolgancha)
    ]
], resize_keyboard=True)

adds_btnss3 = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="Uzbek language"),         # Uzbek tili
        KeyboardButton(text="English"),                # English (qolgancha)
    ],
    [
        KeyboardButton(text="Back"),                   # Orqaga -> Back
    ],
], resize_keyboard=True)


