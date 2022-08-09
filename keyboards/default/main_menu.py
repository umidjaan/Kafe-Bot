from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


asosiy = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍 Buyurtma berish")],
        [KeyboardButton(text="📦 Buyurtmalarim"), KeyboardButton(text="⚙️ Sozlamalar")],
        [KeyboardButton(text="ℹ️ Biz haqimizda"), KeyboardButton(text="✍️ Fikr qoldirish")]
    ],
    resize_keyboard=True
)