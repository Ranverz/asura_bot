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
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await callback_query.message.delete()
            await bot.send_message(chat_id=callback_query.from_user.id, text='Telegram Premium',
                                   reply_markup=kb.keyboard_tg)
        else:
            await callback_query.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='tg_1m_qr')
async def process_callback_button_tg_1m(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await callback_query.message.delete()
            price_tg_1m = await db.show_price('tg_1m')
            await bot.send_message(chat_id=callback_query.from_user.id, text=f'''Товар: 🎈Telegram Premium QR (1 месяц)
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


💵 Цена: {price_tg_1m}₽''',
                                   reply_markup=kb.keyboard_buy_tg_1m)
        else:
            await callback_query.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='tg_1y_qr')
async def process_callback_button_tg_1y(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await callback_query.message.delete()
            price_tg_1y = await db.show_price('tg_1y')
            await bot.send_message(chat_id=callback_query.from_user.id, text=f'''Товар: 🎈Telegram Premium QR (1 год)
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
                                   reply_markup=kb.keyboard_buy_tg_1y)
        else:
            await callback_query.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='tg_back')
async def process_callback_button_tg_back(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await callback_query.message.delete()
            await bot.send_message(chat_id=callback_query.from_user.id, text='Доступные категории в магазине:',
                                   reply_markup=kb.keyboard_stock_inl)
        else:
            await callback_query.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_tg_back')
async def process_callback_button_tg_buy_back(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await callback_query.message.delete()
            await bot.send_message(chat_id=callback_query.from_user.id, text='Telegram Premium',
                                   reply_markup=kb.keyboard_tg)
        else:
            await callback_query.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_buy_tg_1y')
async def process_buy_tg_1y_qr(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_tg_1y_qr = await db.show_price('tg_1y')
            if money >= price_tg_1y_qr:
                await db.add_money(callback_query.from_user.id, -price_tg_1y_qr)
                await db.add_purchase(callback_query.from_user.id, 'Telegram Premium 1y qr', price_tg_1y_qr, time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await callback_query.message.delete()
                await callback_query.message.answer(
                    text=f'''
Поздравляем с покупкой Telegram Premium на 1 год. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв при помощи команды /review
Пример: /review Отличный магазин.

тип товара:Telegram Premium 1 год QR
уникальный номер: {id_p}
                        ''')
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Telegram Premium 1 год QR''')
            else:
                await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
        else:
            await callback_query.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_buy_tg_1m')
async def process_buy_tg_1m_qr(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_tg_1m_qr = await db.show_price('tg_1m')
            if money >= price_tg_1m_qr:
                await db.add_money(callback_query.from_user.id, -price_tg_1m_qr)
                await db.add_purchase(callback_query.from_user.id, 'Telegram Premium 1m qr', price_tg_1m_qr, time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await callback_query.message.delete()
                await callback_query.message.answer(
                    text=f'''
Поздравляем с покупкой Telegram Premium на 1 месяц. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв при помощи команды /review
Пример: /review Отличный магазин.

тип товара:Telegram Premium 1 месяц QR
уникальный номер: {id_p}
                        ''')
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Telegram Premium 1 месяц QR''')
            else:
                await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
        else:
            await callback_query.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(callback_query.from_user.id, 0)


def reg_hand_tg():
    dp.register_callback_query_handler(process_callback_button_tg, text='btntg')
    dp.register_callback_query_handler(process_callback_button_tg_1m, text='tg_1m_qr')
    dp.register_callback_query_handler(process_callback_button_tg_1y, text='tg_1y_qr')
    dp.register_callback_query_handler(process_callback_button_tg_back, text='tg_back')
    dp.register_callback_query_handler(process_callback_button_tg_buy_back, text='buy_tg_back')
    dp.register_callback_query_handler(process_buy_tg_1y_qr, text='buy_buy_tg_1y')
    dp.register_callback_query_handler(process_buy_tg_1m_qr, text='buy_buy_tg_1m')
