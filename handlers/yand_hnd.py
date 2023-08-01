import datetime

from aiogram import types

from app import keyboards as kb
from app.var import bot, dp, moscow_tz, check_sub_channel, NEWS_ID
from app import database as db

from dotenv import load_dotenv
import os

load_dotenv()
op_id = os.getenv('OPERATOR_ID')


# @dp.callback_query_handler(text='btnyandex')
async def process_callback_button_ya(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await callback_query.message.delete()
            price_ya = await db.show_price('ya')
            await bot.send_message(chat_id=callback_query.from_user.id, text=f'''
🎈Яндекс Плюс 3 месяца
📄 Описание: 
Вам не нужно привязывать карту к аккаунту, по истечению подписки списаний не будет!
Это не общий аккаунт. Подпиской будете пользоваться только вы на своём аккаунте. Ваша личная информация никому не видна. Все плейлисты, Кинопоиск и другие сервисы, будут вашими индивидуальными.
Что даёт подписка Яндекс.Плюс можно почитать по ссылке (https://plus.yandex.ru/?through=landing_plus)

📦 Как происходит выдача:
1. Если вы переподключаетесь после окончания предыдущего приглашения перейдите в профиль семьи и нажмите «Это вы» и «Покинуть группу»
2. Войдите в аккаунт яндекса на котором необходима активация (убедитесь что это нужный аккаунт, т.к. замены в случае активации на другом нет)
3. Перейдите по инвайт-ссылке которую вы получите в диалоге с администратором.
4. После проверки ожидаем вашего отзыва.


💵 Цена: {price_ya}₽''',
                                   reply_markup=kb.keyboard_buy_ya)
        else:
            await callback_query.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_ya_back')
async def process_callback_button_ya_back(callback_query: types.CallbackQuery):
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


# @dp.callback_query_handler(text='buy_buy_ya')
async def process_buy_ya(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
            price_ya = await db.show_price('ya')
            if money >= price_ya:
                await db.add_money(callback_query.from_user.id, -price_ya)
                await db.add_purchase(callback_query.from_user.id, 'Яндекс Плюс 3 месяца', price_ya, time)
                id_p = await db.show_purchase_id(callback_query.from_user.id, time)
                await callback_query.message.delete()
                await callback_query.message.answer(
                    text=f'''
Поздравляем с покупкой Яндекс плюс на 3 месяца. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв при помощи команды /review
Пример: /review Отличный магазин.

тип товара:Яндекс плюс на 3 месяца
уникальный номер: {id_p}
                        ''')
                await bot.send_message(op_id,
                                       f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Яндекс плюс на 3 месяца''')
            else:
                await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
        else:
            await callback_query.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(callback_query.from_user.id, 0)


def reg_hand_ya():
    dp.register_callback_query_handler(process_callback_button_ya, text='btnyandex')
    dp.register_callback_query_handler(process_callback_button_ya_back, text='buy_ya_back')
    dp.register_callback_query_handler(process_buy_ya, text='buy_buy_ya')
