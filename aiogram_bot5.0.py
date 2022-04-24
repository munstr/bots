from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import json
import os 
import asyncio
import time
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils import config as cfg
from pyowm.utils.config import get_default_config
import wikipedia
import re


#переменные
bot = Bot('5254391359:AAHHzp56Sx79SP0q9MrsRc3klaXwUAk21Do')
dp = Dispatcher(bot)
punctuation = '.,?¿!¡(){}<>[]:;=≈≠+±-¯—–_*×÷/|\\~%^#&№%‰"„“«»”\'ʼ‹‡`†›$€₽¥¢£'
admsend = []
idd = '1983759935'
pluszn = False
minuszn = False
umnozzn = False
delenzn = False
weather = False
wikip = False

#кнопки
inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Сложение', callback_data='plus')).add(InlineKeyboardButton(text='Вычитание', callback_data='minus')).add(InlineKeyboardButton(text='Умножение', callback_data='umnoz')).add(InlineKeyboardButton(text='Деление', callback_data='delen'))


#обработка запрещенных слов
def get_words(text, punctuation=punctuation):
    text = text.lower()
    for c in punctuation:
        text = text.replace(c, ' ')
    words = set(text.split(' '))
    if '' in words:
        words.remove('')
    return words

def weatherr(place):
    global weather
    global clouds
    global temperat
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = OWM('e3a6bb0af106f781e5bac08fd23945cc')
    mgr = owm.weather_manager()

    try:
        observation = mgr.weather_at_place(place)
        w = observation.weather
        clouds = w.detailed_status      # 'clouds'
        temperat = w.temperature('celsius')['temp']
        weather = False
    except:
        clouds = ''
        temperat = 0
        weather = True


#хэндлерЫ
@dp.message_handler(commands=['start'])
async def hellgho(message: types.Message):
    await message.answer('Привет. Я на связи)')
    
@dp.message_handler(commands=['calc'])
async def hellgo(message: types.Message):
    await message.answer('Режим калькулятора активирован.')
    await message.answer('Выберите действие:', reply_markup=inkb)
    await message.answer('Введите первое и второе число через пробелы')
    
@dp.callback_query_handler(text='plus')
async def pluscatttlc(callback : types.CallbackQuery):
    global pluszn
    pluszn = True
    
    
@dp.callback_query_handler(text='minus')
async def pluscakjklc(callback : types.CallbackQuery):
    global minuszn
    minuszn = True
  
@dp.callback_query_handler(text='umnoz')
async def pluscjjjalc(callback : types.CallbackQuery):
    global umnozzn
    umnozzn = True
    
@dp.callback_query_handler(text='delen')
async def pluscalnnnc(callback : types.CallbackQuery):
    global delenzn
    delenzn = True
      
    

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

@dp.message_handler(commands=['weather'])
async def admin_mwwwqode(message: types.Message):
    global weather
    weather = True
    await message.answer('Режим погоды активирован')
    await message.answer('Напишите название вашего города')

@dp.message_handler(commands=['wikipedia'])
async def admin_mwwqode(message: types.Message):
    global wikip
    wikip = True
    await message.answer('Режим поиска по википедии активирован')
    await message.answer('Напишите слово, которое вы хотите найти')


# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")
# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext=ny.content[:1000]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'




@dp.message_handler()
async def echo_send(message : types.Message):
    admsend.append(str(message.from_user.id) + ': ' + message.text)
    if len(get_words(message.text) & set(json.load(open('ukr.json')))) != 0:
        msg = await message.reply('Обсуждение на эту тему ЗАПРЕЩЕНО!!!')
        time.sleep(4)
        await msg.delete()
        await message.delete()
	
    if len(get_words(message.text) & set(json.load(open('mat.json')))) != 0:
        msg = await message.reply('Материться ЗАПРЕЩЕНО!!!')
        time.sleep(4)
        await msg.delete()
        await message.delete()

    global pluszn
    global minuszn
    global umnozzn
    global delenzn
    global wikip
    
    if pluszn == True:
        s = message.text
        try:
            x = int(s.split()[0])
            y = int(s.split()[1])
            otv = x + y
            await message.answer('Ответ: ' + str(otv))
        except ValueError:
            await message.answer('Введите цифры, а не буквы')
        except IndexError:
            await message.answer('Введите 2 числа!!!')
        pluszn = False



    elif minuszn == True: 
        s = message.text
        try:
            x = int(s.split()[0])
            y = int(s.split()[1])
            otv = x - y
            await message.answer('Ответ: ' + str(otv))
        except ValueError:
            await message.answer('Введите цифры, а не буквы')
        except IndexError:
            await message.answer('Введите 2 числа!!!')
        minuszn = False


    elif delenzn == True:
        s = message.text
        try:
            x = int(s.split()[0])
            y = int(s.split()[1])
            otv = x / y
            await message.answer('Ответ: ' + str(otv))
        except ValueError:
            await message.answer('Введите цифры, а не буквы')
        except IndexError:
            await message.answer('Введите 2 числа!!!')
        delenzn = False
            


    elif umnozzn == True:
        s = message.text
        try:
            x = int(s.split()[0])
            y = int(s.split()[1])
            otv = x * y
            await message.answer('Ответ: ' + str(otv))
        except ValueError:
            await message.answer('Введите цифры, а не буквы')
        except IndexError:
            await message.answer('Введите 2 числа!!!')  
        umnozzn = False  

    if weather == True:
        global place 
        place = message.text
        weatherr(place)
        if clouds != '':
            await message.answer('Сегодня в городе ' + place + ' ' + clouds + '\n' + 'Температура в районе ' + str(temperat) + '°C')
        else:
            await message.answer('Данного города нет в базе городов или вы ввели не название города. Попробуйте заново')

    if wikip == True:
        await message.answer(getwiki(message.text))
        wikip = False


        

if __name__ == '__main__':
    executor.start_polling(dp)