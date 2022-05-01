from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils import config as cfg
from pyowm.utils.config import get_default_config
from create_bot import bot, dp, owm
from commhand import weather

weather = False

def weatherr(place):
    global weather
    global clouds
    global temperat
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
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

@dp.message_handler(commands=['weather'])
async def admin_mwwwqode(message: types.Message):
    global weather
    weather = True
    await message.answer('Режим погоды активирован')
    await message.answer('Напишите название вашего города')