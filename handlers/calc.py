from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from create_bot import bot, dp, owm

pluszn = False
minuszn = False
umnozzn = False
delenzn = False


inkb = InlineKeyboardMarkup(row_width=1)\
.add(InlineKeyboardButton(text='Сложение', callback_data='plus'))\
.add(InlineKeyboardButton(text='Вычитание', callback_data='minus'))\
.add(InlineKeyboardButton(text='Умножение', callback_data='umnoz'))\
.add(InlineKeyboardButton(text='Деление', callback_data='delen'))


@dp.message_handler(commands=['calc'])
async def hellgo(message: types.Message):
    await message.answer('Режим калькулятора активирован.')
    await message.answer('Выберите действие:', reply_markup=inkb)
    
    
@dp.callback_query_handler(text='plus')
async def pluscatttlc(callback : types.CallbackQuery):
    global pluszn
    pluszn = True
    await callback.message.answer('Введите первое и второе число через пробелы')
    await callback.answer()
    
    
@dp.callback_query_handler(text='minus')
async def pluscakjklc(callback : types.CallbackQuery):
    global minuszn
    minuszn = True
    await callback.message.answer('Введите первое и второе число через пробелы')
    await callback.answer()
  
@dp.callback_query_handler(text='umnoz')
async def pluscjjjalc(callback : types.CallbackQuery):
    global umnozzn
    umnozzn = True
    await callback.message.answer('Введите первое и второе число через пробелы')
    await callback.answer()
    
@dp.callback_query_handler(text='delen')
async def pluscalnnnc(callback : types.CallbackQuery):
    global delenzn
    delenzn = True
    await callback.message.answer('Введите первое и второе число через пробелы')
    await callback.answer()
