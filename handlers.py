from aiogram import types, Dispatcher
import commands


def redistred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start_bot, commands=['start'])
