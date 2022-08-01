import logging
from aiogram import Bot,Dispatcher,executor,types

API_TOKEN = '5425002217:AAHFvK3mJr4fpy4z4xZUqgIdrcfFkq_qvBA'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async  def start(message:types.Message):
    await message.reply('Salom \nBu bot sizga Ism,Username va ID qaytaradi') 
    
@dp.message_handler(commands=['help'])
async  def help(message:types.Message):
    await message.reply('Sizga qanday yordam kerak') 

@dp.message_handler()
async  def javob(message:types.Message):
        await message.answer(message.text) 

   
if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)