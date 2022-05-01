from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import time
import json
from create_bot import bot, dp, owm
from wikip import getwiki, wikip
from calc import pluszn, minuszn, umnozzn, delenzn
from weather import weather, weatherr

admsend = []
punctuation = '.,?¿!¡(){}<>[]:;=≈≠+±-¯—–_*×÷/|\\~%^#&№%‰"„“«»”\'ʼ‹‡`†›$€₽¥¢£'

#обработка запрещенных слов
def get_words(text, punctuation=punctuation):
    text = text.lower()
    for c in punctuation:
        text = text.replace(c, ' ')
    words = set(text.split(' '))
    if '' in words:
        words.remove('')
    return words

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
            pluszn = False
        except ValueError:
            await message.answer('Введите цифры, а не буквы')
        except IndexError:
            await message.answer('Введите 2 числа!!!')
        



    elif minuszn == True: 
        s = message.text
        try:
            x = int(s.split()[0])
            y = int(s.split()[1])
            otv = x - y
            await message.answer('Ответ: ' + str(otv))
            minuszn = False
        except ValueError:
            await message.answer('Введите цифры, а не буквы')
        except IndexError:
            await message.answer('Введите 2 числа!!!')
        


    elif delenzn == True:
        s = message.text
        try:
            x = int(s.split()[0])
            y = int(s.split()[1])
            otv = x / y
            await message.answer('Ответ: ' + str(otv))
            delenzn = False
        except ValueError:
            await message.answer('Введите цифры, а не буквы')
        except IndexError:
            await message.answer('Введите 2 числа!!!')
        
            


    elif umnozzn == True:
        s = message.text
        try:
            x = int(s.split()[0])
            y = int(s.split()[1])
            otv = x * y
            await message.answer('Ответ: ' + str(otv))
            umnozzn = False 
        except ValueError:
            await message.answer('Введите цифры, а не буквы')
        except IndexError:
            await message.answer('Введите 2 числа!!!')  
         

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