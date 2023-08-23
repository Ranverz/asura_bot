import datetime

from aiogram import types

from app import keyboards as kb
from app.var import bot, dp, moscow_tz, check_sub_channel, NEWS_ID
from app import database as db

from dotenv import load_dotenv
import os

load_dotenv()
op_id = os.getenv('OPERATOR_ID')


async def process_callback_button_fortnite(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text=f'''🎈Fortnite В-баксы
📄 Описание: 
В-баксы на Ваш аккаунт Fortnite. Для активации потребуется данные для входа в Ваш аккаунт XBOX.

Аккаунт XBOX должен быть привязан к аккаунту Epic Games.
Если аккаунт XBOX привязан не к тому аккаунту Epic Games, после выполнения заказа мы НЕ СМОЖЕМ вам вернуть деньги.

❗️Отвязывать Xbox аккаунт от учетной записи Epic Games не рекомендуется во избежании обнуления В-Баксов, оставляете привязку как есть.''',
                                        reply_markup=kb.keyboard_fortnite,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def process_callback_fortnite_1000(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price = await db.show_price('fortnite_1000')
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text=f'''
🎈Fortnite 1000 В-баксов
❗️Аккаунт XBOX должен быть привязан к аккаунту Epic Games

💵 Цена: {price}₽
''',
                                        reply_markup=kb.keyboard_buy_fortnite_1000,
                                        message_id=callback_query.message.message_id)


async def process_callback_fortnite_2800(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price = await db.show_price('fortnite_2800')
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text=f'''
🎈Fortnite 2800 В-баксов
❗️Аккаунт XBOX должен быть привязан к аккаунту Epic Games

💵 Цена: {price}₽
''',
                                        reply_markup=kb.keyboard_buy_fortnite_2800,
                                        message_id=callback_query.message.message_id)


async def process_callback_fortnite_5000(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price = await db.show_price('fortnite_5000')
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text=f'''
🎈Fortnite 5000 В-баксов
❗️Аккаунт XBOX должен быть привязан к аккаунту Epic Games

💵 Цена: {price}₽
''',
                                        reply_markup=kb.keyboard_buy_fortnite_5000,
                                        message_id=callback_query.message.message_id)


async def process_callback_fortnite_13500(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price = await db.show_price('fortnite_13500')
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text=f'''
🎈Fortnite 13500 В-баксов
❗️Аккаунт XBOX должен быть привязан к аккаунту Epic Games

💵 Цена: {price}₽
''',
                                        reply_markup=kb.keyboard_buy_fortnite_13500,
                                        message_id=callback_query.message.message_id)


async def process_buy_fortnite_1000(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price = await db.show_price('fortnite_1000')
            if money >= price:
                await db.add_money(callback_query.from_user.id, -price)
                await db.add_purchase(callback_query.from_user.id, '1000 В-баксов',
                                      price,
                                      time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой 1000 В-баксов. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв.

тип товара:1000 В-баксов
уникальный номер: {id_p}
                        ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:1000 В-баксов''')
            else:
                await callback_query.message.answer(
                    text=f'Недостаточно средств, сначала пополните баланс\nНе хватает {price - money}₽')
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def process_buy_fortnite_2800(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price = await db.show_price('fortnite_2800')
            if money >= price:
                await db.add_money(callback_query.from_user.id, -price)
                await db.add_purchase(callback_query.from_user.id, '2800 В-баксов',
                                      price,
                                      time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой 2800 В-баксов. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв.

тип товара:2800 В-баксов
уникальный номер: {id_p}
                        ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:2800 В-баксов''')
            else:
                await callback_query.message.answer(
                    text=f'Недостаточно средств, сначала пополните баланс\nНе хватает {price - money}₽')
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def process_buy_fortnite_5000(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price = await db.show_price('fortnite_5000')
            if money >= price:
                await db.add_money(callback_query.from_user.id, -price)
                await db.add_purchase(callback_query.from_user.id, '5000 В-баксов',
                                      price,
                                      time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой 5000 В-баксов. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв.

тип товара:5000 В-баксов
уникальный номер: {id_p}
                        ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:5000 В-баксов''')
            else:
                await callback_query.message.answer(
                    text=f'Недостаточно средств, сначала пополните баланс\nНе хватает {price - money}₽')
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def process_buy_fortnite_13500(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price = await db.show_price('fortnite_13500')
            if money >= price:
                await db.add_money(callback_query.from_user.id, -price)
                await db.add_purchase(callback_query.from_user.id, '13500 В-баксов',
                                      price,
                                      time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой 13500 В-баксов. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв.

тип товара:13500 В-баксов
уникальный номер: {id_p}
                        ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:13500 В-баксов''')
            else:
                await callback_query.message.answer(
                    text=f'Недостаточно средств, сначала пополните баланс\nНе хватает {price - money}₽')
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def process_callback_button_fortnite_back(callback_query: types.CallbackQuery):
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


def reg_hand_fortnite():
    dp.register_callback_query_handler(process_callback_button_fortnite, text='btnfortnite')
    dp.register_callback_query_handler(process_callback_button_fortnite, text='buy_fortnite_back')
    dp.register_callback_query_handler(process_callback_button_fortnite_back, text='fortnite_back')

    dp.register_callback_query_handler(process_callback_fortnite_1000, text='fortnite_1000')
    dp.register_callback_query_handler(process_callback_fortnite_2800, text='fortnite_2800')
    dp.register_callback_query_handler(process_callback_fortnite_5000, text='fortnite_5000')
    dp.register_callback_query_handler(process_callback_fortnite_13500, text='fortnite_13500')

    dp.register_callback_query_handler(process_buy_fortnite_1000, text='buy_buy_fortnite_1000')
    dp.register_callback_query_handler(process_buy_fortnite_2800, text='buy_buy_fortnite_2800')
    dp.register_callback_query_handler(process_buy_fortnite_5000, text='buy_buy_fortnite_5000')
    dp.register_callback_query_handler(process_buy_fortnite_13500, text='buy_buy_fortnite_13500')
