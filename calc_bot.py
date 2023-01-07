import time
import logging


from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

TOKEN= "5800074540:AAEsGbzeQT_fsDK1UhuqJNae_uHLVWPxPSA"
msg="{} Работает!"

bot= Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['help','start'])
async def start_handler(message: types.Message):
    user_id=message.from_user.id
    user_name=message.from_user.first_name
    logging.info(f"{user_id=} {user_name=} {time.asctime()}")

    await message.reply(f"Привет {user_name}, этот бот выполняет функцию калькулятора для простых и комплексных чисел, для того что бы получить ответ отправьте боту выражение, например (1 + 2j)+(3 + 4j) ")
    
@dp.message_handler()
async def calc(message: types.Message):
    await message.reply(eval(message.text))


k1= KeyboardButton("/start")
k2= KeyboardButton('/help')

kb_client=ReplyKeyboardMarkup()
kb_client.add(k2).add(k1)

print("start")

executor.start_polling(dp)