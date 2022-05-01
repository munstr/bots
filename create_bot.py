from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from pyowm import OWM

bot = Bot('5148976681:AAH_2G4SmbegCm3VMjh54bxDJ3SILT6FhXc')
dp = Dispatcher(bot)
owm = OWM('e3a6bb0af106f781e5bac08fd23945cc')