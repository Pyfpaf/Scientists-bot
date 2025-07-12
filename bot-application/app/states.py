from aiogram.fsm.state import StatesGroup, State


class Chatai(StatesGroup):
    text = State()
    wait = State()


class GigaChat(StatesGroup):
    text = State()
    wait = State()
