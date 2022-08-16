from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

markup = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [InlineKeyboardButton(text="⬅️", callback_data="prev"), InlineKeyboardButton(text="💰", callback_data="pay"), InlineKeyboardButton(text="➡️", callback_data="next")]
    ])