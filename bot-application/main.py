import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommandScopeAllPrivateChats, BotCommand

from core import settings
from app import router
from utils import cmds_list


async def main():
    bot = Bot(token=settings.token.bot)
    dp = Dispatcher()
    dp.include_routers(router)

    # Данная команда удаляет все сообщения, которые пришли на сервер во время выключенного бота
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(
        commands=cmds_list,
        scope=BotCommandScopeAllPrivateChats(),
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
