from aiogram.dispatcher.filters.state import StatesGroup, State


class Kafe(StatesGroup):
    cats = State()
    sub_cat = State()
    product = State()