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

NEWS_ID = '@tigigiitjg'
REVIEWS_ID = '@asurastore_reviews'


async def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False
