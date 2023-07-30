from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import pytz

from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(token=os.getenv("TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

moscow_tz = pytz.timezone('Europe/Moscow')

price_nitro_1m = 349
price_nitro_1y = 3399

price_nitro_1m_qr = 349
price_nitro_1y_qr = 3399

price_nitro_1m_noreg = 439
price_nitro_1y_noreg = 3599

price_moon = 410
price_60k = 90
price_300k = 410
price_980k = 1240
price_1980k = 2690
price_3280k = 4140
price_6480k = 8280

price_sp = 440
# oneiric shard
price_hon_60k = 110
price_hon_300k = 440
price_hon_980k = 1320
price_hon_1980k = 2860
price_hon_3280k = 4400
price_hon_6480k = 8800

NEWS_ID = '@asurastore_news'
REVIEWS_ID = '@asurastore_reviews'


async def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False
