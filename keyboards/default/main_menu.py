from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


asosiy = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="đ Buyurtma berish")],
        [KeyboardButton(text="đĻ Buyurtmalarim"), KeyboardButton(text="âšī¸ Biz haqimizda")],
        # [KeyboardButton(text="âī¸ Sozlamalar"), KeyboardButton(text="âī¸ Fikr qoldirish")]
    ],
    resize_keyboard=True
)