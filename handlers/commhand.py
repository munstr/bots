from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import random
from create_bot import bot, dp, owm

idd = '1983759935'

#хэндлерЫ
@dp.message_handler(commands=['start'])
async def hellgho(message: types.Message):
    await message.answer('Привет. Я на связи)')

@dp.message_handler(commands=['random'])
async def hellgewho(message: types.Message):
    await message.answer('Случайное число от 1 до 10: ' + str(random.randrange(1, 11, 1)))

@dp.message_handler(commands=['coin'])
async def hellwwho(message: types.Message):
    result = random.randint (1, 2)
    if result == 1:
        await message.answer('РЕШКА')
    elif result == 2:
        await message.answer('ОРЕЛ')
    


@dp.message_handler(commands=['about'])
async def admin_mdddodwwe(message: types.Message):  
    await message.answer('ChatBot - последняя версия от 29.04.2022\nНаписано на Python\nРазработчик: @munstr001') 

@dp.message_handler(commands=['info'])
async def adodwwe(message: types.Message):  
    await message.answer('Вероятность события: ' + str(random.randrange(0, 101, 1)) + '%')
    

#админская часть
@dp.message_handler(commands=['send_all_message'])
async def admin_modwwe(message: types.Message):
    if str(message.from_user.id) == idd: 
        await message.answer('Привет, админ')
        number = len(admsend)        
        for name in admsend:
            await message.answer(name)
        admsend.clear()
    else:
        await message.answer("Вы не админ")



