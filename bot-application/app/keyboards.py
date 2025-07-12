from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="OpenAI"), KeyboardButton(text="GigaChat")]],
    resize_keyboard=True,
    input_field_placeholder="Выберите модель AI",
)
