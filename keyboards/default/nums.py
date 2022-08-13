from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

digits = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

for i in range(1, 10):
    digits.insert(KeyboardButton(text=str(i)))
digits.add(KeyboardButton(text="📥 Savatcha"), KeyboardButton(text="◀️ Orqaga"))

contact = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[KeyboardButton(text="✅ Raqamni tasdiqlash", request_contact=True)]])

location = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[KeyboardButton(text="📍 Joylashuvni yuborish", request_location=True)]])