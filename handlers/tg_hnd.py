import datetime

from aiogram import types

from app import keyboards as kb
from app.var import bot, dp, moscow_tz, check_sub_channel, NEWS_ID
from app import database as db

from dotenv import load_dotenv
import os

load_dotenv()
op_id = os.getenv('OPERATOR_ID')


# @dp.callback_query_handler(text='btntg')
async def process_callback_button_tg(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text='Telegram Premium',
                                        reply_markup=kb.keyboard_tg, message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='tg_1m_qr')
async def process_callback_button_tg_1m_qr(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_tg_1m_qr = await db.show_price('tg_1m_qr')
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text=f'''Товар: 🎈Telegram Premium QR (1 месяц)
📄 Описание: 
🎈Телеграм Премиум — это эксклюзивная подписка, которая дарит уникальные преимущества:
• Значок подписчика: Премиум-пользователи видны по звездочке возле имени.
• Отключение рекламы: Никакой раздражающей рекламы, наслаждайтесь чистым контентом.
• Увеличенные лимиты: Загружайте файлы до 4 Гб, создавайте 20 папок с 200 чатами, сохраняйте 400 гифок.
• Максимальная скорость скачивания: Загружайте файлы с максимальной скоростью интернета.
• Распознавание голосовых сообщений: Войсы автоматически переводятся в текст.
• Управление чатами: Выбирайте папку по умолчанию, автоматическое перемещение новых чатов.
• Эксклюзивные анимированные стикеры: Уникальные стикеры с полноэкранными анимациями.
• Уникальные реакции: Более 10 новых эмодзи для выражения эмоций.
• Активные видеоаватары: Анимированные аватары проигрываются в списках чатов.
• После покупки Вам приходит официальный чек на почту, поэтому не будет никаких блокировок и наказаний. Все легально.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и отправляет вам QR code который необходимо отсканировать для того чтоб мы вошли на ваш аккаунт.
Мы приобретаем подписку на свою личную карту.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.


💵 Цена: {price_tg_1m_qr}₽''',
                                        reply_markup=kb.keyboard_buy_tg_1m_qr,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='tg_1m_noreg')
async def process_callback_button_tg_1m_noreg(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_tg_1m_noreg = await db.show_price('tg_1m_noreg')
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text=f'''Товар: 🎈Telegram Premium (1 месяц)
📄 Описание: 
🎈Телеграм Премиум — это эксклюзивная подписка, которая дарит уникальные преимущества:
• Значок подписчика: Премиум-пользователи видны по звездочке возле имени.
• Отключение рекламы: Никакой раздражающей рекламы, наслаждайтесь чистым контентом.
• Увеличенные лимиты: Загружайте файлы до 4 Гб, создавайте 20 папок с 200 чатами, сохраняйте 400 гифок.
• Максимальная скорость скачивания: Загружайте файлы с максимальной скоростью интернета.
• Распознавание голосовых сообщений: Войсы автоматически переводятся в текст.
• Управление чатами: Выбирайте папку по умолчанию, автоматическое перемещение новых чатов.
• Эксклюзивные анимированные стикеры: Уникальные стикеры с полноэкранными анимациями.
• Уникальные реакции: Более 10 новых эмодзи для выражения эмоций.
• Активные видеоаватары: Анимированные аватары проигрываются в списках чатов.
• После покупки Вам приходит официальный чек на почту, поэтому не будет никаких блокировок и наказаний. Все легально.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и отправляет вам инструкцию по получению Telegram Premium.
После проверки ожидаем вашего отзыва.


💵 Цена: {price_tg_1m_noreg}₽''',
                                        reply_markup=kb.keyboard_buy_tg_1m_noreg,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='tg_1y_qr')
async def process_callback_button_tg_1y_qr(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_tg_1y = await db.show_price('tg_1y_qr')
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text=f'''Товар: 🎈Telegram Premium QR (1 год)
📄 Описание: 
🎈Телеграм Премиум — это эксклюзивная подписка, которая дарит уникальные преимущества:
• Значок подписчика: Премиум-пользователи видны по звездочке возле имени.
• Отключение рекламы: Никакой раздражающей рекламы, наслаждайтесь чистым контентом.
• Увеличенные лимиты: Загружайте файлы до 4 Гб, создавайте 20 папок с 200 чатами, сохраняйте 400 гифок.
• Максимальная скорость скачивания: Загружайте файлы с максимальной скоростью интернета.
• Распознавание голосовых сообщений: Войсы автоматически переводятся в текст.
• Управление чатами: Выбирайте папку по умолчанию, автоматическое перемещение новых чатов.
• Эксклюзивные анимированные стикеры: Уникальные стикеры с полноэкранными анимациями.
• Уникальные реакции: Более 10 новых эмодзи для выражения эмоций.
• Активные видеоаватары: Анимированные аватары проигрываются в списках чатов.
• После покупки Вам приходит официальный чек на почту, поэтому не будет никаких блокировок и наказаний. Все легально.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и отправляет вам QR code который необходимо отсканировать для того чтоб мы вошли на ваш аккаунт.
Мы приобретаем подписку на свою личную карту.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.


💵 Цена: {price_tg_1y}₽''',
                                        reply_markup=kb.keyboard_buy_tg_1y_qr,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='tg_1y_noreg')
async def process_callback_button_tg_1y_noreg(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            price_tg_1y_noreg = await db.show_price('tg_1y_noreg')
            await bot.edit_message_text(chat_id=callback_query.from_user.id, text=f'''Товар: 🎈Telegram Premium (1 месяц)
📄 Описание: 
🎈Телеграм Премиум — это эксклюзивная подписка, которая дарит уникальные преимущества:
• Значок подписчика: Премиум-пользователи видны по звездочке возле имени.
• Отключение рекламы: Никакой раздражающей рекламы, наслаждайтесь чистым контентом.
• Увеличенные лимиты: Загружайте файлы до 4 Гб, создавайте 20 папок с 200 чатами, сохраняйте 400 гифок.
• Максимальная скорость скачивания: Загружайте файлы с максимальной скоростью интернета.
• Распознавание голосовых сообщений: Войсы автоматически переводятся в текст.
• Управление чатами: Выбирайте папку по умолчанию, автоматическое перемещение новых чатов.
• Эксклюзивные анимированные стикеры: Уникальные стикеры с полноэкранными анимациями.
• Уникальные реакции: Более 10 новых эмодзи для выражения эмоций.
• Активные видеоаватары: Анимированные аватары проигрываются в списках чатов.
• После покупки Вам приходит официальный чек на почту, поэтому не будет никаких блокировок и наказаний. Все легально.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и отправляет вам инструкцию по получению Telegram Premium.
После проверки ожидаем вашего отзыва.


💵 Цена: {price_tg_1y_noreg}₽''',
                                        reply_markup=kb.keyboard_buy_tg_1y_noreg,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='tg_back')
async def process_callback_button_tg_back(callback_query: types.CallbackQuery):
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


# @dp.callback_query_handler(text='buy_buy_tg_1y')
async def process_buy_tg_1y_qr(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_tg_1y_qr = await db.show_price('tg_1y_qr')
            if money >= price_tg_1y_qr:
                await db.add_money(callback_query.from_user.id, -price_tg_1y_qr)
                await db.add_purchase(callback_query.from_user.id, 'Telegram Premium 1 год QR', price_tg_1y_qr, time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой Telegram Premium на 1 год. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, если он не написал вам сам.

уникальный номер: {id_p}
                        ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Telegram Premium 1 год QR''')
            else:
                await callback_query.message.answer(
                    text=f'Недостаточно средств, сначала пополните баланс\nНе хватает {price_tg_1y_qr - money}₽',
                    reply_markup=kb.keyboard_top_up)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_buy_tg_1y_noreg')
async def process_buy_tg_1y_noreg(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_tg_1y_noreg = await db.show_price('tg_1y_noreg')
            if money >= price_tg_1y_noreg:
                await db.add_money(callback_query.from_user.id, -price_tg_1y_noreg)
                await db.add_purchase(callback_query.from_user.id, 'Telegram Premium 1 год без входа',
                                      price_tg_1y_noreg,
                                      time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой Telegram Premium на 1 год. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, если он не написал вам сам.

уникальный номер: {id_p}
                        ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Telegram Premium 1 год без входа''')
            else:
                await callback_query.message.answer(
                    text=f'Недостаточно средств, сначала пополните баланс\nНе хватает {price_tg_1y_noreg - money}₽',
                    reply_markup=kb.keyboard_top_up)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_buy_tg_1m_qr')
async def process_buy_tg_1m_qr(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_tg_1m_qr = await db.show_price('tg_1m_qr')
            if money >= price_tg_1m_qr:
                await db.add_money(callback_query.from_user.id, -price_tg_1m_qr)
                await db.add_purchase(callback_query.from_user.id, 'Telegram Premium 1 месяц QR', price_tg_1m_qr, time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой Telegram Premium на 1 месяц. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, если он не написал вам сам.

уникальный номер: {id_p}
                        ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Telegram Premium 1 месяц QR''')
            else:
                await callback_query.message.answer(
                    text=f'Недостаточно средств, сначала пополните баланс\nНе хватает {price_tg_1m_qr - money}₽',
                    reply_markup=kb.keyboard_top_up)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_buy_tg_1m_noreg')
async def process_buy_tg_1m_noreg(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_tg_1m_noreg = await db.show_price('tg_1m_noreg')
            if money >= price_tg_1m_noreg:
                await db.add_money(callback_query.from_user.id, -price_tg_1m_noreg)
                await db.add_purchase(callback_query.from_user.id, 'Telegram Premium 1 месяц без входа',
                                      price_tg_1m_noreg,
                                      time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await bot.edit_message_text(
                    text=f'''
Поздравляем с покупкой Telegram Premium на 1 месяц. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, если он не написал вам сам.

уникальный номер: {id_p}
                        ''', reply_markup=kb.review_kb(id_p), chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.message_id)
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Telegram Premium 1 месяц без входа''')
            else:
                await callback_query.message.answer(
                    text=f'Недостаточно средств, сначала пополните баланс\nНе хватает {price_tg_1m_noreg - money}₽',
                    reply_markup=kb.keyboard_top_up)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


def reg_hand_tg():
    dp.register_callback_query_handler(process_callback_button_tg, text='btntg')
    dp.register_callback_query_handler(process_callback_button_tg, text='buy_tg_back')
    dp.register_callback_query_handler(process_callback_button_tg_1m_qr, text='tg_1m_qr')
    dp.register_callback_query_handler(process_callback_button_tg_1y_qr, text='tg_1y_qr')
    dp.register_callback_query_handler(process_callback_button_tg_1m_noreg, text='tg_1m_noreg')
    dp.register_callback_query_handler(process_callback_button_tg_1y_noreg, text='tg_1y_noreg')
    dp.register_callback_query_handler(process_callback_button_tg_back, text='tg_back')
    dp.register_callback_query_handler(process_buy_tg_1y_qr, text='buy_buy_tg_1y_qr')
    dp.register_callback_query_handler(process_buy_tg_1m_qr, text='buy_buy_tg_1m_qr')
    dp.register_callback_query_handler(process_buy_tg_1y_noreg, text='buy_buy_tg_1y_noreg')
    dp.register_callback_query_handler(process_buy_tg_1m_noreg, text='buy_buy_tg_1m_noreg')
