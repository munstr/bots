from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from pyowm import OWM

bot = Bot('')
dp = Dispatcher(bot)
owm = OWM('e3a6bb0af106f781e5bac08fd23945cc')