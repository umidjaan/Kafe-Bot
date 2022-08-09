from aiogram import types
from keyboards.default.cats import cats_keyboard
from loader import dp, db
from states.holat import Kafe
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


@dp.message_handler(text="🛍 Buyurtma berish")
async def bot_echo(message: types.Message):
    await message.answer("Nimadan boshlaymiz?", reply_markup=cats_keyboard)
    await Kafe.cats.set()


@dp.message_handler(state=Kafe.cats)
async def get_sub_cats(message: types.Message):
    cat = message.text
    sub_cat_id = db.select_sub_cat_id(name=cat)[0]
    sub_cats = db.select_all_sub_cats(cat_id=sub_cat_id)
    if len(sub_cats) == 0:
        await message.answer("Ma'lumot topilmadi")
    else:
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for i in sub_cats:
            markup.insert(KeyboardButton(text=i[0]))
        await message.answer(f"Choose subcategory", reply_markup=markup)
        await Kafe.next()
