from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from aiogram import types

import pytz

from dotenv import load_dotenv
import os

import datetime

from app import keyboards as kb
from app import database as db

load_dotenv()
bot = Bot(token=os.getenv("TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
op_id = os.getenv('OPERATOR_ID')

moscow_tz = pytz.timezone('Europe/Moscow')

NEWS_ID = 'asurastore_news'
REVIEWS_ID = 'asurastore_reviews'


async def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False


async def show_item_prev_buy(item_in_db, item_name, description, reply_kb, callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price = await db.show_price(item_in_db)
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text=f'''
🎈{item_name}
📄 Описание: {description}


💵 Цена: {price}₽''',
                                        reply_markup=reply_kb,
                                        message_id=callback_query.message.message_id, parse_mode=ParseMode.HTML,
                                        disable_web_page_preview=True)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def confirm_item_buy(item_in_db, item_name, callback_query: types.CallbackQuery, ):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price = await db.show_price(item_in_db)
            if money >= price:
                await db.add_money(callback_query.from_user.id, -price)
                await db.add_purchase(callback_query.from_user.id, item_name, price,
                                      time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой {item_name}. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, если он не написал вам сам.

уникальный номер: {id_p}
                            ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:{item_name}''')
            else:
                await callback_query.message.answer(
                    text=f'Недостаточно средств, сначала пополните баланс\nНе хватает {price - money}₽',
                    reply_markup=kb.keyboard_top_up)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)
