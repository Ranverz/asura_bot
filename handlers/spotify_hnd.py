import datetime

from aiogram import types

from app import keyboards as kb
from app.var import bot, dp, moscow_tz, check_sub_channel, NEWS_ID
from app import database as db

from dotenv import load_dotenv
import os

load_dotenv()
op_id = os.getenv('OPERATOR_ID')


async def process_callback_button_spotify(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text='''
🎈 Spotify Premium

📄 Описание: 
Ваша музыка. Ваши плейлисты. Доступ к зарубежным и отечественным исполнителям. Никакой рекламы.
Все это снова доступно без VPN!''',
                                        reply_markup=kb.keyboard_spotify,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def process_callback_button_spotify_1m(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_spotify_1m = await db.show_price('spotify_1m')
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text=f'''
🎈 Spotify Premium(1 месяц)

📄 Описание: 
Подписка Spotify Premium на один месяц на ваш аккаунт.

💵 Цена: {price_spotify_1m}₽''',
                                        reply_markup=kb.keyboard_buy_spotify_1m,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def process_callback_button_spotify_3m(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_spotify_3m = await db.show_price('spotify_3m')
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text=f'''
🎈 Spotify Premium(3 месяца)

📄 Описание: 
Подписка Spotify Premium на три месяца на ваш аккаунт.

💵 Цена: {price_spotify_3m}₽''',
                                        reply_markup=kb.keyboard_buy_spotify_3m,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def process_callback_button_spotify_6m(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_spotify_6m = await db.show_price('spotify_6m')
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text=f'''
🎈 Spotify Premium(6 месяцев)

📄 Описание: 
Подписка Spotify Premium на шесть месяцев на ваш аккаунт.

💵 Цена: {price_spotify_6m}₽''',
                                        reply_markup=kb.keyboard_buy_spotify_6m,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def process_callback_button_spotify_12m(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_spotify_12m = await db.show_price('spotify_12m')
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text=f'''
🎈 Spotify Premium(12 месяцев)

📄 Описание: 
Подписка Spotify Premium на двенадцать месяцев на ваш аккаунт.

💵 Цена: {price_spotify_12m}₽''',
                                        reply_markup=kb.keyboard_buy_spotify_12m,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def process_callback_button_spotify_back(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text='Доступные категории в магазине:',
                                        reply_markup=kb.keyboard_stock_inl,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def process_buy_spotify_1m(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_spotify_1m = await db.show_price('spotify_1m')
            if money >= price_spotify_1m:
                await db.add_money(callback_query.from_user.id, -price_spotify_1m)
                await db.add_purchase(callback_query.from_user.id, 'Spotify Premium 1 месяц',
                                      price_spotify_1m,
                                      time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой Spotify Premium на 1 месяц. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, если он не написал вам сам.

уникальный номер: {id_p}
                        ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Spotify Premium 1 месяц''')
            else:
                await callback_query.message.answer(
                    text=f'Недостаточно средств, сначала пополните баланс\nНе хватает {price_spotify_1m - money}₽')
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def process_buy_spotify_3m(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_spotify_3m = await db.show_price('spotify_3m')
            if money >= price_spotify_3m:
                await db.add_money(callback_query.from_user.id, -price_spotify_3m)
                await db.add_purchase(callback_query.from_user.id, 'Spotify Premium 3 месяца',
                                      price_spotify_3m,
                                      time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой Spotify Premium на 3 месяца. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, если он не написал вам сам.

уникальный номер: {id_p}
                        ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Spotify Premium 3 месяца''')
            else:
                await callback_query.message.answer(
                    text=f'Недостаточно средств, сначала пополните баланс\nНе хватает {price_spotify_3m - money}₽',
                    reply_markup=kb.keyboard_top_up)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def process_buy_spotify_6m(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_spotify_6m = await db.show_price('spotify_6m')
            if money >= price_spotify_6m:
                await db.add_money(callback_query.from_user.id, -price_spotify_6m)
                await db.add_purchase(callback_query.from_user.id, 'Spotify Premium 6 месяц',
                                      price_spotify_6m,
                                      time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой Spotify Premium на 6 месяцев. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, если он не написал вам сам.

уникальный номер: {id_p}
                        ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Spotify Premium 6 месяц''')
            else:
                await callback_query.message.answer(
                    text=f'Недостаточно средств, сначала пополните баланс\nНе хватает {price_spotify_6m - money}₽',
                    reply_markup=kb.keyboard_top_up)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def process_buy_spotify_12m(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_spotify_12m = await db.show_price('spotify_12m')
            if money >= price_spotify_12m:
                await db.add_money(callback_query.from_user.id, -price_spotify_12m)
                await db.add_purchase(callback_query.from_user.id, 'Spotify Premium 12 месяцев',
                                      price_spotify_12m,
                                      time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой Spotify Premium на 12 месяцев. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, если он не написал вам сам.

уникальный номер: {id_p}
                        ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Spotify Premium 12 месяцев''')
            else:
                await callback_query.message.answer(
                    text=f'Недостаточно средств, сначала пополните баланс\nНе хватает {price_spotify_12m - money}₽',
                    reply_markup=kb.keyboard_top_up)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


def reg_hand_spotify():
    dp.register_callback_query_handler(process_callback_button_spotify, text='btnspotify')
    dp.register_callback_query_handler(process_callback_button_spotify, text='buy_spotify_back')
    dp.register_callback_query_handler(process_callback_button_spotify_back, text='spotify_back')
    dp.register_callback_query_handler(process_callback_button_spotify_1m, text='spotify_1m')
    dp.register_callback_query_handler(process_callback_button_spotify_3m, text='spotify_3m')
    dp.register_callback_query_handler(process_callback_button_spotify_6m, text='spotify_6m')
    dp.register_callback_query_handler(process_callback_button_spotify_12m, text='spotify_12m')
    dp.register_callback_query_handler(process_buy_spotify_1m, text='buy_buy_spotify_1m')
    dp.register_callback_query_handler(process_buy_spotify_3m, text='buy_buy_spotify_3m')
    dp.register_callback_query_handler(process_buy_spotify_6m, text='buy_buy_spotify_6m')
    dp.register_callback_query_handler(process_buy_spotify_12m, text='buy_buy_spotify_12m')
