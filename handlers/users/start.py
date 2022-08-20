import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS, CHANNELS
from loader import dp, db, bot
from keyboards.default.main_menu import asosiy
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        if not db.select_user(id=message.from_user.id):
            markup = InlineKeyboardMarkup(row_width=1)
            for channel in CHANNELS:
                chat = await bot.get_chat(channel)
                invite_link = await chat.export_invite_link()
                markup.insert(InlineKeyboardButton(text=f"{chat.title}", url=invite_link))
            
            markup.add(InlineKeyboardButton(text="✔️ Obunani tekshirish", callback_data="check_subs"))
            await message.answer("Quyidagi kanallarga obuna bo'ling", reply_markup=markup)
            db.add_user(id=message.from_user.id,
                        name=name)
            # Adminga xabar beramiz
            count = db.count_users()[0]
            msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
            await bot.send_message(chat_id=ADMINS[0], text=msg)
        else:
            await message.answer(f"Xush kelibsiz! {message.from_user.full_name}", reply_markup=asosiy)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        await message.answer(f"Xush kelibsiz! {name}", reply_markup=asosiy)
