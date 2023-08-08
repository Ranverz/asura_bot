import datetime

from aiogram import types

from app import keyboards as kb
from app.var import bot, dp, moscow_tz, check_sub_channel, NEWS_ID
from app import database as db

from dotenv import load_dotenv
import os

load_dotenv()
op_id = os.getenv('OPERATOR_ID')


# @dp.callback_query_handler(text='btngenshin')
async def btg(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text='Genshin Impact',
                                        reply_markup=kb.keyboard_genshin, message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='gnsh_moon')
async def pr_gnsh_moon(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_moon = await db.show_price('gnsh_moon')
            await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                        text=f'''Товар: 
🎈Благословение полой луны

📄 Описание: 
🎈При каждой покупке Благословения полой луны вы получаете 300 Кристалов Сотворения и 30 дней Благословения.
В течение 30 дней ежедневно при входе в игру вы будете получать 90 камней истока(Обновляется ежедневно в 04:00 GMT+1)

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и запрашивает UID от вашего аккаунта, для покупки благословения полой луны вам на аккаунт.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.

💵 Цена: {price_moon}₽''',
                                        reply_markup=kb.keyboard_genshin_moon,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='gnsh_60k')
async def pr_gnsh_60k(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_60k = await db.show_price('gnsh_60k')
            await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                        text=f'''Товар: 
🎈60 Кристаллов Сотворения

📄 Описание: 
🎈Кристаллы сотворения - особая валюта в игре Genshin Impact, которую вы можете обменять на Камни Истока с курсом 1:1, или же потратить на внутриигровую косметику.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и запрашивает UID от вашего аккаунта, для покупки кристаллов вам на аккаунт.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.

Если у вас на аккаунте доступен 2x бонус первой покупки, то он сработает и вы получите в два раза больше Кристаллов Сотворения(120).

💵 Цена: {price_60k}₽''',
                                        reply_markup=kb.keyboard_genshin_60k,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='gnsh_300k')
async def pr_gnsh_300k(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_300k = await db.show_price('gnsh_300k')
            await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                        text=f'''Товар: 
🎈300+30 Кристаллов Сотворения

📄 Описание: 
🎈Кристаллы сотворения - особая валюта в игре Genshin Impact, которую вы можете обменять на Камни Истока с курсом 1:1, или же потратить на внутриигровую косметику.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и запрашивает UID от вашего аккаунта, для покупки кристаллов вам на аккаунт.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.

Если у вас на аккаунте доступен 2x бонус первой покупки, то он сработает и вы получите в два раза больше Кристаллов Сотворения(600).

💵 Цена: {price_300k}₽''',
                                        reply_markup=kb.keyboard_genshin_300k,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='gnsh_980k')
async def pr_gnsh_980k(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_980k = await db.show_price('gnsh_980k')
            await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                        text=f'''Товар: 
🎈980+110 Кристаллов Сотворения

📄 Описание: 
🎈Кристаллы сотворения - особая валюта в игре Genshin Impact, которую вы можете обменять на Камни Истока с курсом 1:1, или же потратить на внутриигровую косметику.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и запрашивает UID от вашего аккаунта, для покупки кристаллов вам на аккаунт.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.

Если у вас на аккаунте доступен 2x бонус первой покупки, то он сработает и вы получите в два раза больше Кристаллов Сотворения(1960).

💵 Цена: {price_980k}₽''',
                                        reply_markup=kb.keyboard_genshin_980k,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='gnsh_1980k')
async def pr_gnsh_1980k(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_1980k = await db.show_price('gnsh_1980k')
            await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                        text=f'''Товар: 
🎈1980+260 Кристаллов Сотворения

📄 Описание: 
🎈Кристаллы сотворения - особая валюта в игре Genshin Impact, которую вы можете обменять на Камни Истока с курсом 1:1, или же потратить на внутриигровую косметику.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и запрашивает UID от вашего аккаунта, для покупки кристаллов вам на аккаунт.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.

Если у вас на аккаунте доступен 2x бонус первой покупки, то он сработает и вы получите в два раза больше Кристаллов Сотворения(3960).

💵 Цена: {price_1980k}₽''',
                                        reply_markup=kb.keyboard_genshin_1980k,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='gnsh_3280k')
async def pr_gnsh_3280k(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_3280k = await db.show_price('gnsh_3280k')
            await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                        text=f'''Товар: 
🎈3280 + 600 Кристаллов Сотворения

📄 Описание: 
🎈Кристаллы сотворения - особая валюта в игре Genshin Impact, которую вы можете обменять на Камни Истока с курсом 1:1, или же потратить на внутриигровую косметику.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и запрашивает UID от вашего аккаунта, для покупки кристаллов вам на аккаунт.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.

Если у вас на аккаунте доступен 2x бонус первой покупки, то он сработает и вы получите в два раза больше Кристаллов Сотворения(6560).

💵 Цена: {price_3280k}₽''',
                                        reply_markup=kb.keyboard_genshin_3280k,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='gnsh_6480k')
async def pr_gnsh_6480k(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_6480k = await db.show_price('gnsh_6480k')
            await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                        text=f'''Товар: 
🎈6480 + 1600 Кристаллов Сотворения

📄 Описание: 
🎈Кристаллы сотворения - особая валюта в игре Genshin Impact, которую вы можете обменять на Камни Истока с курсом 1:1, или же потратить на внутриигровую косметику.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и запрашивает UID от вашего аккаунта, для покупки кристаллов вам на аккаунт.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.

Если у вас на аккаунте доступен 2x бонус первой покупки, то он сработает и вы получите в два раза больше Кристаллов Сотворения(12960).

💵 Цена: {price_6480k}₽''',
                                        reply_markup=kb.keyboard_genshin_6480k,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='gnsh_back')
async def pr_gnsh_back(callback_query: types.CallbackQuery):
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


# @dp.callback_query_handler(text='buy_gnsh_back')
async def pr_gnsh_buy_back(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text='Genshin Impact',
                                        reply_markup=kb.keyboard_genshin, message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_gnsh_moon')
async def pr_gnsh_buy_moon(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_moon = await db.show_price('gnsh_moon')
            if money >= price_moon:
                await db.add_money(callback_query.from_user.id, -price_moon)
                await db.add_purchase(callback_query.from_user.id, 'Благословение полой луны', price_moon, time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой Благословения полой луны. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв.

тип товара:Благословение полой луны
уникальный номер: {id_p}
                ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Благословение полой луны(uid)''')
            else:
                await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_gnsh_60k')
async def pr_gnsh_buy_60k(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_60k = await db.show_price('gnsh_60k')
            if money >= price_60k:
                await db.add_money(callback_query.from_user.id, -price_60k)
                await db.add_purchase(callback_query.from_user.id, '60 Кристаллов Сотворения', price_60k, time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой 60 Кристаллов Сотворения. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв.

тип товара:60 Кристаллов Сотворения
уникальный номер: {id_p}
                ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:60 Кристаллов Сотворения(uid)''')
            else:
                await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_gnsh_300k')
async def pr_gnsh_buy_300k(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_300k = await db.show_price('gnsh_300k')
            if money >= price_300k:
                await db.add_money(callback_query.from_user.id, -price_300k)
                await db.add_purchase(callback_query.from_user.id, '300+30 Кристаллов Сотворения', price_300k, time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой 300+30 Кристаллов Сотворения. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв.

тип товара:300+30 Кристаллов Сотворения
уникальный номер: {id_p}
                ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:300+30 Кристаллов Сотворения(uid)''')
            else:
                await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_gnsh_980k')
async def pr_gnsh_buy_980k(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_980k = await db.show_price('gnsh_980k')
            if money >= price_980k:
                await db.add_money(callback_query.from_user.id, -price_980k)
                await db.add_purchase(callback_query.from_user.id, '980+110 Кристаллов Сотворения', price_980k, time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой 980+110 Кристаллов Сотворения. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв.

тип товара:980+110 Кристаллов Сотворения
уникальный номер: {id_p}
                ''', reply_markup=kb.review_kb(id_p), message_id=callback_query.message.message_id,
                    chat_id=callback_query.message.chat.id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:980+110 Кристаллов Сотворения(uid)''')
            else:
                await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_gnsh_1980k')
async def pr_gnsh_buy_1980k(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_1980k = await db.show_price('gnsh_1980k')
            if money >= price_1980k:
                await db.add_money(callback_query.from_user.id, -price_1980k)
                await db.add_purchase(callback_query.from_user.id, '1980+260 Кристаллов Сотворения', price_1980k, time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой 1980+260 Кристаллов Сотворения. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв.

тип товара:1980+260 Кристаллов Сотворения
уникальный номер: {id_p}
                ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:1980+260 Кристаллов Сотворения(uid)''')
            else:
                await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_gnsh_3280k')
async def pr_gnsh_buy_3280k(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_3280k = await db.show_price('gnsh_3280k')
            if money >= price_3280k:
                await db.add_money(callback_query.from_user.id, -price_3280k)
                await db.add_purchase(callback_query.from_user.id, '3280+600 Кристаллов Сотворения', price_3280k, time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой 3280+600 Кристаллов Сотворения. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв.

тип товара:3280+600 Кристаллов Сотворения
уникальный номер: {id_p}
                ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:3280+600 Кристаллов Сотворения(uid)''')
            else:
                await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_gnsh_6480k')
async def pr_gnsh_buy_6480k(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_6480k = await db.show_price('gnsh_6480k')
            if money >= price_6480k:
                await db.add_money(callback_query.from_user.id, -price_6480k)
                await db.add_purchase(callback_query.from_user.id, '6480+1600 Кристаллов Сотворения', price_6480k, time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой 6480+1600 Кристаллов Сотворения. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв.

тип товара:6480+1600 Кристаллов Сотворения
уникальный номер: {id_p}
                ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:6480+1600 Кристаллов Сотворения(uid)''')
            else:
                await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


def reg_hand_genshin():
    dp.register_callback_query_handler(btg, text='btngenshin')
    dp.register_callback_query_handler(pr_gnsh_back, text='gnsh_back')
    dp.register_callback_query_handler(pr_gnsh_buy_back, text='buy_gnsh_back')
    dp.register_callback_query_handler(pr_gnsh_moon, text='gnsh_moon')
    dp.register_callback_query_handler(pr_gnsh_60k, text='gnsh_60k')
    dp.register_callback_query_handler(pr_gnsh_300k, text='gnsh_300k')
    dp.register_callback_query_handler(pr_gnsh_980k, text='gnsh_980k')
    dp.register_callback_query_handler(pr_gnsh_1980k, text='gnsh_1980k')
    dp.register_callback_query_handler(pr_gnsh_3280k, text='gnsh_3280k')
    dp.register_callback_query_handler(pr_gnsh_6480k, text='gnsh_6480k')

    dp.register_callback_query_handler(pr_gnsh_buy_moon, text='buy_gnsh_moon')
    dp.register_callback_query_handler(pr_gnsh_buy_60k, text='buy_gnsh_60k')
    dp.register_callback_query_handler(pr_gnsh_buy_300k, text='buy_gnsh_300k')
    dp.register_callback_query_handler(pr_gnsh_buy_980k, text='buy_gnsh_980k')
    dp.register_callback_query_handler(pr_gnsh_buy_1980k, text='buy_gnsh_1980k')
    dp.register_callback_query_handler(pr_gnsh_buy_3280k, text='buy_gnsh_3280k')
    dp.register_callback_query_handler(pr_gnsh_buy_6480k, text='buy_gnsh_6480k')
