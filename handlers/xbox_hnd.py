import datetime

from aiogram import types

from app import keyboards as kb
from app.var import bot, dp, moscow_tz, check_sub_channel, NEWS_ID
from app import database as db

from dotenv import load_dotenv
import os

load_dotenv()
op_id = os.getenv('OPERATOR_ID')


# @dp.callback_query_handler(text='btnxbox')
async def process_callback_button_xbox(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await callback_query.message.delete()
            price_xbox = await db.show_price('xbox')
            await bot.send_message(chat_id=callback_query.from_user.id, text=f'''
🎈XBOX GAME PASS ULTIMATE
(если вы хотите купить не на один месяц, то просто сделайте несколько заказов на 1 месяц)
📄 Описание: 
Активация происходит через покупку в интернет-магазине Microsoft - все легально.
Данная подписка подходит для любого региона в том числе и Россия!
Данная подписка подходит для всех аккаунтов , на момент активации не должно быть активных подписок!

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру.
Также нужно будет сообщить данные для успешного входа в Ваш аккаунт Microsoft https://login.live.com (в основном только почту и пароль) - вы можете поменять пароль перед и после заказа, нам Ваш аккаунт нужен только для установки подписки, все легально через магазин майкрософт.
Мы приобретаем подписку на свою личную карту.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.


💵 Цена: {price_xbox}₽''',
                                   reply_markup=kb.keyboard_buy_xbox)
        else:
            await callback_query.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_xbox_back')
async def process_callback_button_xbox_back(callback_query: types.CallbackQuery):
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


# @dp.callback_query_handler(text='buy_buy_xbox')
async def process_buy_xbox(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_xbox = await db.show_price('xbox')
            if money >= price_xbox:
                await db.add_money(callback_query.from_user.id, -price_xbox)
                await db.add_purchase(callback_query.from_user.id, 'Xbox Game Pass 1m', price_xbox, time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await callback_query.message.delete()
                await callback_query.message.answer(
                    text=f'''
Поздравляем с покупкой Xbox Game Pass на 1 месяц. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв.

тип товара:Xbox Game Pass на 1 месяц
уникальный номер: {id_p}
                        ''', reply_markup=kb.review_kb(id_p))
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Xbox Game Pass на 1 месяц''')
            else:
                await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
        else:
            await callback_query.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(callback_query.from_user.id, 0)


def reg_hand_xbox():
    dp.register_callback_query_handler(process_callback_button_xbox, text='btnxbox')
    dp.register_callback_query_handler(process_callback_button_xbox_back, text='buy_xbox_back')
    dp.register_callback_query_handler(process_buy_xbox, text='buy_buy_xbox')
