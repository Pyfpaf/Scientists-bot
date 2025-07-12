from aiogram.types import BotCommand


cmds_list = [
    BotCommand(command="start", description="Начать работу с ботом заново"),
    BotCommand(command="cancel", description="Перейти к выбору моделей AI"),
    BotCommand(command="about", description="Информация о боте"),
]
