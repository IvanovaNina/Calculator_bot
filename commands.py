from config import dp, bot
from aiogram import types
import calculator


@dp.message_handler(commands='start')
async def start_bot(message: types.Message):
    print(message.text)
    print(message)
    await message.answer('Привет! Введите то, что хотите посчитать! ')


@dp.message_handler()
async def start_bot(message: types.Message):
    print(message.text)
    print(message)
    calculator.set_expression(message.text)
    calculator.calculate()
    await message.reply(f' =  {calculator.get_result()}')
