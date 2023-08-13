import datetime

from aiogram import types

from app import keyboards as kb
from app.var import bot, dp, moscow_tz, check_sub_channel, NEWS_ID
from app import database as db

from dotenv import load_dotenv
import os

load_dotenv()
op_id = os.getenv('OPERATOR_ID')


# @dp.callback_query_handler(text='btndiscord')
async def process_callback_button_ds(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(text='Discord Nitro', chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id, reply_markup=kb.keyboard_nitro)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='ntr_1m_no_log')
async def process_callback_button_ds_1m_noreg(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_nitro_1m_noreg = await db.show_price('dsntr_1m_noreg')
            await bot.edit_message_text(text=f'''Товар: 🎈Nitro Full (1 месяц) + 2 boosts
📄 Описание: 
🎈Discord Nitro
• Это новое поколение выдачи Discord Nitro которое не слетает.
• Если у Вас ранее была подписка Discord Nitro, то мы все равно сможем выдать вам новую подписку.
• У Вас не должно быть активной подписки. (Исключение: сможете продлить на год если у Вас активная подписка на месяц)
• После покупки Вам приходит официальный чек на почту, поэтому не будет никаких блокировок и наказаний. Все легально.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и отправляет инструкцию как получить дискорд нитро.
Для покупки подписки мы выдадим вам нашу личную карту и не важно из какой Вы страны.
После проверки ожидаем вашего отзыва.

💵 Цена: {price_nitro_1m_noreg}₽''', chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=kb.keyboard_buy_nitro_1m_noreg)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='ntr_1y_no_log')
async def process_callback_button_ds_1y_noreg(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_nitro_1y_noreg = await db.show_price('dsntr_1y_noreg')
            await bot.edit_message_text(text=f'''Товар: 🎈Nitro Full (1 год) + 2 boosts
📄 Описание: 
🎈Discord Nitro
• Это новое поколение выдачи Discord Nitro которое не слетает.
• Если у Вас ранее была подписка Discord Nitro, то мы все равно сможем выдать вам новую подписку.
• У Вас не должно быть активной подписки. (Исключение: сможете продлить на год если у Вас активная подписка на месяц)
• После покупки Вам приходит официальный чек на почту, поэтому не будет никаких блокировок и наказаний. Все легально.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и отправляет инструкцию как получить дискорд нитро.
Для покупки подписки мы выдадим вам нашу личную карту и не важно из какой Вы страны.
После проверки ожидаем вашего отзыва.

💵 Цена: {price_nitro_1y_noreg}₽''', chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=kb.keyboard_buy_nitro_1y_noreg)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_buy_nitro_1y_qr')
async def process_callback_button_ds_1y_qr(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_nitro_1y_qr = await db.show_price('dsntr_1y_qr')
            await bot.edit_message_text(text=f''' Товар: 🎈Nitro Full (1 год) + 2 boosts
📄 Описание: 
🎈Discord Nitro QR
• Это новое поколение выдачи Discord Nitro которое не слетает.
• Если у Вас ранее была подписка Discord Nitro, то мы все равно сможем выдать вам новую подписку.
• У Вас не должно быть активной подписки. (Исключение: можем продлить на год если у Вас активная подписка на месяц)
• После покупки Вам приходит официальный чек на почту, поэтому не будет никаких блокировок и наказаний. Все легально.
    
📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и отправляет вам QR code который необходимо отсканировать для того чтоб мы вошли на ваш аккаунт.
Мы приобретаем подписку на свою личную карту и не важно из какой Вы страны.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.
Так же рекомендуем сменить пароль после проверки получения подписки для дополнительной безопасности.

🛡Не беспокойтесь, ваши данные в безопасности и не будут переданы третьим лицам. Мы не запрашиваем Ваш логин и пароль, так как эти данные персональные и не должны распространяться, а QR code перестает работать через 2 минуты и не содержит Ваш логин и пароль.
Мы работаем в браузерах с запретом сбора данных куки и т.п. для безопасности вашего аккаунта и данных.

💵 Цена: {price_nitro_1y_qr}₽
    ''', chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                                        reply_markup=kb.keyboard_buy_nitro_1y_qr)

        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_buy_nitro_1m_qr')
async def process_callback_button_ds_1m_qr(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_nitro_1m_qr = await db.show_price('dsntr_1m_qr')
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text=f''' Товар: 🎈Nitro Full (1 месяц) + 2 boosts
📄 Описание: 
🎈Discord Nitro QR
• Это новое поколение выдачи Discord Nitro которое не слетает.
• Если у Вас ранее была подписка Discord Nitro, то мы все равно сможем выдать вам новую подписку.
• У Вас не должно быть активной подписки. (Исключение: можем продлить на год если у Вас активная подписка на месяц)
• После покупки Вам приходит официальный чек на почту, поэтому не будет никаких блокировок и наказаний. Все легально.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и отправляет вам QR code который необходимо отсканировать для того чтоб мы вошли на ваш аккаунт.
Мы приобретаем подписку на свою личную карту и не важно из какой Вы страны.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.
Так же рекомендуем сменить пароль после проверки получения подписки для дополнительной безопасности.

🛡Не беспокойтесь, ваши данные в безопасности и не будут переданы третьим лицам. Мы не запрашиваем Ваш логин и пароль, так как эти данные персональные и не должны распространяться, а QR code перестает работать через 2 минуты и не содержит Ваш логин и пароль.
Мы работаем в браузерах с запретом сбора данных куки и т.п. для безопасности вашего аккаунта и данных.

💵 Цена: {price_nitro_1m_qr}₽

''',
                                        reply_markup=kb.keyboard_buy_nitro_1m_qr,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='ntr_back')
async def process_callback_button_ds_back(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                        message_id=callback_query.message.message_id,
                                        text='Доступные категории в магазине:',
                                        reply_markup=kb.keyboard_stock_inl)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_back')
async def process_callback_button_ds_buy_back(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                        message_id=callback_query.message.message_id, text='Discord nitro',
                                        reply_markup=kb.keyboard_nitro)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_buy_nitro_1y_qr')
async def process_buy_nitro_1y_qr(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_nitro_1y_qr = await db.show_price('dsntr_1y_qr')
            if money >= price_nitro_1y_qr:
                await db.add_money(callback_query.from_user.id, -price_nitro_1y_qr)
                await db.add_purchase(callback_query.from_user.id, 'Discord Nitro 1y QR', price_nitro_1y_qr, time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой Discord Nitro на 1 год. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв.

тип товара:Discord Nitro 1 год QR
уникальный номер: {id_p}
                            ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Discord Nitro 1 год QR''')
            else:
                await callback_query.message.answer(
                    text=f'Недостаточно средств, сначала пополните баланс\nНе хватает {price_nitro_1y_qr - money}₽')
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_buy_nitro_1m_qr')
async def process_buy_nitro_1m_qr(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_nitro_1m_qr = await db.show_price('dsntr_1m_qr')
            if money >= price_nitro_1m_qr:
                await db.add_money(callback_query.from_user.id, -price_nitro_1m_qr)
                await db.add_purchase(callback_query.from_user.id, 'Discord Nitro 1m QR', price_nitro_1m_qr, time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой Discord Nitro на 1 месяц. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв.

тип товара:Discord Nitro 1 месяц QR
уникальный номер: {id_p}
                            ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Discord Nitro 1 месяц QR''')
            else:
                await callback_query.message.answer(
                    text=f'Недостаточно средств, сначала пополните баланс\nНе хватает {price_nitro_1m_qr - money}₽')
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_buy_nitro_1m_noreg')
async def process_buy_nitro_1m_noreg(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_nitro_1m_noreg = await db.show_price('dsntr_1m_noreg')
            if money >= price_nitro_1m_noreg:
                await db.add_money(callback_query.from_user.id, -price_nitro_1m_noreg)
                await db.add_purchase(callback_query.from_user.id, 'Discord Nitro 1m noreg', price_nitro_1m_noreg, time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой Discord Nitro на 1 месяц. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.
    
Убедительная просьба после получения товара оставить отзыв.
    
тип товара:Discord Nitro 1 месяц без входа
уникальный номер: {id_p}
                                            ''', reply_markup=kb.review_kb(id_p),
                    chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Discord Nitro 1 месяц без входа''')
            else:
                await callback_query.message.answer(
                    text=f'Недостаточно средств, сначала пополните баланс\nНе хватает {price_nitro_1m_noreg - money}₽')
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_buy_nitro_1y_noreg')
async def process_buy_nitro_1y_noreg(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_nitro_1y_noreg = await db.show_price('dsntr_1y_noreg')
            if money >= price_nitro_1y_noreg:
                await db.add_money(callback_query.from_user.id, -price_nitro_1y_noreg)
                await db.add_purchase(callback_query.from_user.id, 'Discord Nitro 1y noreg', price_nitro_1y_noreg, time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой Discord Nitro на 1 год. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.
    
Убедительная просьба после получения товара оставить отзыв.
    
тип товара:Discord Nitro 1 год без входа
уникальный номер: {id_p}
                                            ''', reply_markup=kb.review_kb(id_p),
                    chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Discord Nitro 1 год без входа''')
            else:
                await callback_query.message.answer(
                    text=f'Недостаточно средств, сначала пополните баланс\nНе хватает {price_nitro_1y_noreg - money}₽')
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


def reg_hand_discord():
    dp.register_callback_query_handler(process_buy_nitro_1m_qr, text='buy_buy_nitro_1m_qr')
    dp.register_callback_query_handler(process_buy_nitro_1y_qr, text='buy_buy_nitro_1y_qr')
    dp.register_callback_query_handler(process_buy_nitro_1m_noreg, text='buy_buy_nitro_1m_noreg')
    dp.register_callback_query_handler(process_buy_nitro_1y_noreg, text='buy_buy_nitro_1y_noreg')
    dp.register_callback_query_handler(process_callback_button_ds, text='btndiscord')
    dp.register_callback_query_handler(process_callback_button_ds_1y_qr, text='ntr_1y_qr')
    dp.register_callback_query_handler(process_callback_button_ds_1m_qr, text='ntr_1m_qr')
    dp.register_callback_query_handler(process_callback_button_ds_1m_noreg, text='ntr_1m_no_log')
    dp.register_callback_query_handler(process_callback_button_ds_1y_noreg, text='ntr_1y_no_log')
    dp.register_callback_query_handler(process_callback_button_ds_back, text='ntr_back')
    dp.register_callback_query_handler(process_callback_button_ds_buy_back, text='buy_back')
