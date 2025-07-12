from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from core import generate_llm_query

from .keyboards import main as main_kb
from .states import Chatai, GigaChat

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать!", reply_markup=main_kb)


@router.message(F.text == "OpenAI")
async def openai_chat(message: Message, state: FSMContext):
    await state.set_state(Chatai.text)
    await message.answer("Введите Ваш запрос")


@router.message(Chatai.text)
async def chatai_resp(message: Message, state: FSMContext):
    await state.set_state(Chatai.wait)
    # response = await gpt_text(message.text, 'gpt-3.5-turbo')
    # await message.answer(response)
    await message.answer(message.text)
    await message.answer("Данная модель отключена. Воспользуйтесь моделью Giga Chat ")
    await state.clear()


@router.message(Chatai.wait)
async def chatai_wait(message: Message):
    await message.answer("Подождите, сообщение генерируется")


@router.message(F.text == "GigaChat")
async def giga_chat(message: Message, state: FSMContext):
    await state.set_state(GigaChat.text)
    await message.answer("Введите Ваш запрос")


@router.message(GigaChat.text)
async def giga_chat_resp(message: Message, state: FSMContext):
    await state.set_state(GigaChat.wait)
    response = await generate_llm_query(message.text)
    await message.answer(response)
    await state.clear()


@router.message(GigaChat.wait)
async def giga_chat_wait(message: Message):
    await message.answer("Подождите, сообщение генерируется")
