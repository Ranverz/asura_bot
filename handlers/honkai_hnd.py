import datetime

from aiogram import types

from app import keyboards as kb
from app.var import bot, dp, moscow_tz, check_sub_channel, NEWS_ID
from app import database as db

from dotenv import load_dotenv
import os

load_dotenv()
op_id = os.getenv('OPERATOR_ID')


# @dp.callback_query_handler(text='btnhonkai')
async def btg(callback_query: types.CallbackQuery):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
        await db.set_active(callback_query.from_user.id, 1)
        await callback_query.message.delete()
        await bot.send_message(chat_id=callback_query.from_user.id, text='Honkai: Star Rail',
                               reply_markup=kb.keyboard_honkai)
    else:
        await callback_query.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='hon_sp')
async def pr_hon_sp(callback_query: types.CallbackQuery):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
        await db.set_active(callback_query.from_user.id, 1)
        await callback_query.message.delete()
        price_sp = await db.show_price('hon_sp')
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f'''Товар: 
🎈Пропуск снабжения экспресса

📄 Описание: 
🎈При каждой покупке Пропуска снабжения экспресса вы получаете 300 Сущности древних снов, а срок действия Пропуска снабжения экспресса продлится на 30 дней.
Пока действует Пропуск снабжения экспресса, ежедневно при входе в игру вы будете получать 90 Звездного нефрита(Обновляется ежедневно в 04:00 GMT+1)

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и запрашивает UID от вашего аккаунта, для покупки Пропуска снабжения экспресса вам на аккаунт.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.

💵 Цена: {price_sp}₽''',
                               reply_markup=kb.keyboard_hon_sp)
    else:
        await callback_query.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='hon_60k')
async def pr_hon_60k(callback_query: types.CallbackQuery):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
        await db.set_active(callback_query.from_user.id, 1)
        await callback_query.message.delete()
        price_hon_60k = await db.show_price('hon_60k')
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f'''Товар: 
🎈60 Сущности древних снов

📄 Описание: 
🎈Сущности древних снов - особая валюта в игре Honkai: Star Rail, которую вы можете обменять на Звездный нефрит с курсом 1:1, или же потратить на внутриигровую косметику.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и запрашивает UID от вашего аккаунта, для покупки Сущности древних снов вам на аккаунт.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.

Если у вас на аккаунте доступен 2x бонус первой покупки, то он сработает и вы получите в два раза больше Сущности древних снов(120).

💵 Цена: {price_hon_60k}₽''',
                               reply_markup=kb.keyboard_hon_60k)
    else:
        await callback_query.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='hon_300k')
async def pr_hon_300k(callback_query: types.CallbackQuery):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
        await db.set_active(callback_query.from_user.id, 1)
        await callback_query.message.delete()
        price_hon_300k = await db.show_price('hon_300k')
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f'''Товар: 
🎈300+30 Сущности древних снов

📄 Описание: 
🎈Сущности древних снов - особая валюта в игре Honkai: Star Rail, которую вы можете обменять на Звездный нефрит с курсом 1:1, или же потратить на внутриигровую косметику.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и запрашивает UID от вашего аккаунта, для покупки Сущности древних снов вам на аккаунт.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.

Если у вас на аккаунте доступен 2x бонус первой покупки, то он сработает и вы получите в два раза больше Сущности древних снов(600).

💵 Цена: {price_hon_300k}₽''',
                               reply_markup=kb.keyboard_hon_300k)
    else:
        await callback_query.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='hon_980k')
async def pr_hon_980k(callback_query: types.CallbackQuery):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
        await db.set_active(callback_query.from_user.id, 1)
        await callback_query.message.delete()
        price_hon_980k = await db.show_price('hon_980k')
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f'''Товар: 
🎈980+110 Сущности древних снов

📄 Описание: 
🎈Сущности древних снов - особая валюта в игре Honkai: Star Rail, которую вы можете обменять на Звездный нефрит с курсом 1:1, или же потратить на внутриигровую косметику.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и запрашивает UID от вашего аккаунта, для покупки Сущности древних снов вам на аккаунт.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.

Если у вас на аккаунте доступен 2x бонус первой покупки, то он сработает и вы получите в два раза больше Сущности древних снов(1960).

💵 Цена: {price_hon_980k}₽''',
                               reply_markup=kb.keyboard_hon_980k)
    else:
        await callback_query.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='hon_1980k')
async def pr_hon_1980k(callback_query: types.CallbackQuery):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
        await db.set_active(callback_query.from_user.id, 1)
        await callback_query.message.delete()
        price_hon_1980k = await db.show_price('hon_1980k')
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f'''Товар: 
🎈1980+260 Сущности древних снов

📄 Описание: 
🎈Сущности древних снов - особая валюта в игре Honkai: Star Rail, которую вы можете обменять на Звездный нефрит с курсом 1:1, или же потратить на внутриигровую косметику.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и запрашивает UID от вашего аккаунта, для покупки Сущности древних снов вам на аккаунт.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.

Если у вас на аккаунте доступен 2x бонус первой покупки, то он сработает и вы получите в два раза больше Сущности древних снов(3960).

💵 Цена: {price_hon_1980k}₽''',
                               reply_markup=kb.keyboard_hon_1980k)
    else:
        await callback_query.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='hon_3280k')
async def pr_hon_3280k(callback_query: types.CallbackQuery):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
        await db.set_active(callback_query.from_user.id, 1)
        await callback_query.message.delete()
        price_hon_3280k = await db.show_price('hon_3280k')
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f'''Товар: 
🎈3280+600 Сущности древних снов

📄 Описание: 
🎈Сущности древних снов - особая валюта в игре Honkai: Star Rail, которую вы можете обменять на Звездный нефрит с курсом 1:1, или же потратить на внутриигровую косметику.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и запрашивает UID от вашего аккаунта, для покупки Сущности древних снов вам на аккаунт.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.

Если у вас на аккаунте доступен 2x бонус первой покупки, то он сработает и вы получите в два раза больше Сущности древних снов(6560).

💵 Цена: {price_hon_3280k}₽''',
                               reply_markup=kb.keyboard_hon_3280k)
    else:
        await callback_query.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='hon_6480k')
async def pr_hon_6480k(callback_query: types.CallbackQuery):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
        await db.set_active(callback_query.from_user.id, 1)
        await callback_query.message.delete()
        price_hon_6480k = await db.show_price('hon_6480k')
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f'''Товар: 
🎈6480+1600 Сущности древних снов

📄 Описание: 
🎈Сущности древних снов - особая валюта в игре Honkai: Star Rail, которую вы можете обменять на Звездный нефрит с курсом 1:1, или же потратить на внутриигровую косметику.

📦 Как происходит выдача:
После приобретения товара вы получаете код, который вам необходимо отправить нашему менеджеру. После чего наш менеджер переходит к вам в диалог и запрашивает UID от вашего аккаунта, для покупки Сущности древних снов вам на аккаунт.
Сообщаем Вам о готовности и после проверки ожидаем вашего отзыва.

Если у вас на аккаунте доступен 2x бонус первой покупки, то он сработает и вы получите в два раза больше Сущности древних снов(12960).

💵 Цена: {price_hon_6480k}₽''',
                               reply_markup=kb.keyboard_hon_6480k)
    else:
        await callback_query.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='hon_back')
async def pr_hon_back(callback_query: types.CallbackQuery):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
        await db.set_active(callback_query.from_user.id, 1)
        await callback_query.message.delete()
        await bot.send_message(chat_id=callback_query.from_user.id, text='Доступные категории в магазине:',
                               reply_markup=kb.keyboard_stock_inl)
    else:
        await callback_query.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_hon_back')
async def pr_hon_buy_back(callback_query: types.CallbackQuery):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
        await db.set_active(callback_query.from_user.id, 1)
        await callback_query.message.delete()
        await bot.send_message(chat_id=callback_query.from_user.id, text='Honkai: Star Rail',
                               reply_markup=kb.keyboard_honkai)
    else:
        await callback_query.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_hon_sp')
async def pr_hon_buy_sp(callback_query: types.CallbackQuery):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
        await db.set_active(callback_query.from_user.id, 1)
        money = await db.show_money(callback_query.from_user.id)
        time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
        price_sp = await db.show_price('hon_sp')
        if money >= price_sp:
            await db.add_money(callback_query.from_user.id, -price_sp)
            await db.add_purchase(callback_query.from_user.id, 'Пропуск снабжения экспресса', price_sp, time)
            id_p = await db.show_purchase_id(callback_query.from_user.id, time)
            await callback_query.message.delete()
            await callback_query.message.answer(
                text=f'''
Поздравляем с покупкой Пропуска снабжения экспресса. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв при помощи команды /review
Пример: /review Отличный магазин.

тип товара:Пропуск снабжения экспресса
уникальный номер: {id_p}
            ''')
            await bot.send_message(op_id,
                                   f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:Пропуск снабжения экспресса(uid)''')
        else:
            await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
    else:
        await callback_query.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_hon_6hon
async def pr_hon_buy_60k(callback_query: types.CallbackQuery):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
        await db.set_active(callback_query.from_user.id, 1)
        money = await db.show_money(callback_query.from_user.id)
        time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
        price_hon_60k = await db.show_price('hon_60k')
        if money >= price_hon_60k:
            await db.add_money(callback_query.from_user.id, -price_hon_60k)
            await db.add_purchase(callback_query.from_user.id, '60 Сущности древних снов', price_hon_60k, time)
            id_p = await db.show_purchase_id(callback_query.from_user.id, time)
            await callback_query.message.delete()
            await callback_query.message.answer(
                text=f'''
Поздравляем с покупкой 60 Сущности древних снов. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв при помощи команды /review
Пример: /review Отличный магазин.

тип товара:60 Сущности древних снов
уникальный номер: {id_p}
            ''')
            await bot.send_message(op_id,
                                   f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:60 Сущности древних снов(uid)''')
        else:
            await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
    else:
        await callback_query.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_hon_300k')
async def pr_hon_buy_300k(callback_query: types.CallbackQuery):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
        await db.set_active(callback_query.from_user.id, 1)
        money = await db.show_money(callback_query.from_user.id)
        time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
        price_hon_300k = await db.show_price('hon_300k')
        if money >= price_hon_300k:
            await db.add_money(callback_query.from_user.id, -price_hon_300k)
            await db.add_purchase(callback_query.from_user.id, '300+30 Сущности древних снов', price_hon_300k, time)
            id_p = await db.show_purchase_id(callback_query.from_user.id, time)
            await callback_query.message.delete()
            await callback_query.message.answer(
                text=f'''
Поздравляем с покупкой 300+30 Сущности древних снов. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв при помощи команды /review
Пример: /review Отличный магазин.

тип товара:300+30 Сущности древних снов
уникальный номер: {id_p}
            ''')
            await bot.send_message(op_id,
                                   f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:300+30 Сущности древних снов(uid)''')
        else:
            await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
    else:
        await callback_query.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_hon_980k')
async def pr_hon_buy_980k(callback_query: types.CallbackQuery):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
        await db.set_active(callback_query.from_user.id, 1)
        money = await db.show_money(callback_query.from_user.id)
        time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
        price_hon_980k = await db.show_price('hon_980k')
        if money >= price_hon_980k:
            await db.add_money(callback_query.from_user.id, -price_hon_980k)
            await db.add_purchase(callback_query.from_user.id, '980+110 Сущности древних снов', price_hon_980k, time)
            id_p = await db.show_purchase_id(callback_query.from_user.id, time)
            await callback_query.message.delete()
            await callback_query.message.answer(
                text=f'''
Поздравляем с покупкой 980+110 Сущности древних снов. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв при помощи команды /review
Пример: /review Отличный магазин.

тип товара:980+110 Сущности древних снов
уникальный номер: {id_p}
            ''')
            await bot.send_message(op_id,
                                   f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:980+110 Сущности древних снов(uid)''')
        else:
            await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
    else:
        await callback_query.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_hon_1980k')
async def pr_hon_buy_1980k(callback_query: types.CallbackQuery):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
        await db.set_active(callback_query.from_user.id, 1)
        money = await db.show_money(callback_query.from_user.id)
        time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
        price_hon_1980k = await db.show_price('hon_1980k')
        if money >= price_hon_1980k:
            await db.add_money(callback_query.from_user.id, -price_hon_1980k)
            await db.add_purchase(callback_query.from_user.id, '1980+260 Сущности древних снов', price_hon_1980k, time)
            id_p = await db.show_purchase_id(callback_query.from_user.id, time)
            await callback_query.message.delete()
            await callback_query.message.answer(
                text=f'''
Поздравляем с покупкой 1980+260 Сущности древних снов. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв при помощи команды /review
Пример: /review Отличный магазин.

тип товара:1980+260 Сущности древних снов
уникальный номер: {id_p}
            ''')
            await bot.send_message(op_id,
                                   f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:1980+260 Сущности древних снов(uid)''')
        else:
            await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
    else:
        await callback_query.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_hon_3280k')
async def pr_hon_buy_3280k(callback_query: types.CallbackQuery):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
        await db.set_active(callback_query.from_user.id, 1)
        money = await db.show_money(callback_query.from_user.id)
        time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
        price_hon_3280k = await db.show_price('hon_3280k')
        if money >= price_hon_3280k:
            await db.add_money(callback_query.from_user.id, -price_hon_3280k)
            await db.add_purchase(callback_query.from_user.id, '3280+600 Сущности древних снов', price_hon_3280k, time)
            id_p = await db.show_purchase_id(callback_query.from_user.id, time)
            await callback_query.message.delete()
            await callback_query.message.answer(
                text=f'''
Поздравляем с покупкой 3280+600 Сущности древних снов. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв при помощи команды /review
Пример: /review Отличный магазин.

тип товара:3280+600 Сущности древних снов
уникальный номер: {id_p}
            ''')
            await bot.send_message(op_id,
                                   f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:3280+600 Сущности древних снов(uid)''')
        else:
            await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
    else:
        await callback_query.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(callback_query.from_user.id, 0)


# @dp.callback_query_handler(text='buy_hon_6480k')
async def pr_hon_buy_6480k(callback_query: types.CallbackQuery):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
        await db.set_active(callback_query.from_user.id, 1)
        money = await db.show_money(callback_query.from_user.id)
        time = str(datetime.datetime.now(moscow_tz)).split('+')[0]
        price_hon_6480k = await db.show_price('hon_6480k')
        if money >= price_hon_6480k:
            await db.add_money(callback_query.from_user.id, -price_hon_6480k)
            await db.add_purchase(callback_query.from_user.id, '6480+1600 Сущности древних снов', price_hon_6480k, time)
            id_p = await db.show_purchase_id(callback_query.from_user.id, time)
            await callback_query.message.delete()
            await callback_query.message.answer(
                text=f'''
Поздравляем с покупкой 6480+1600 Сущности древних снов. 
Cвяжитесь с администратором для получения товара: @AsuraStore_helper, переслав это сообщение.

Убедительная просьба после получения товара оставить отзыв при помощи команды /review
Пример: /review Отличный магазин.

тип товара:6480+1600 Сущности древних снов
уникальный номер: {id_p}
            ''')
            await bot.send_message(op_id,
                                   f'''Новый заказ от {callback_query.from_user.full_name}\n@{callback_query.from_user.username}\nid_user: {callback_query.from_user.id}\n\nid_purc: {id_p}\nтип товара:6480+1600 Сущности древних снов(uid)''')
        else:
            await callback_query.message.answer(text='Недостаточно средств, сначала пополните счет')
    else:
        await callback_query.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(callback_query.from_user.id, 0)


def reg_hand_honkai():
    dp.register_callback_query_handler(btg, text='btnhonkai')
    dp.register_callback_query_handler(pr_hon_back, text='hon_back')
    dp.register_callback_query_handler(pr_hon_buy_back, text='buy_hon_back')
    dp.register_callback_query_handler(pr_hon_sp, text='hon_sp')
    dp.register_callback_query_handler(pr_hon_60k, text='hon_60k')
    dp.register_callback_query_handler(pr_hon_300k, text='hon_300k')
    dp.register_callback_query_handler(pr_hon_980k, text='hon_980k')
    dp.register_callback_query_handler(pr_hon_1980k, text='hon_1980k')
    dp.register_callback_query_handler(pr_hon_3280k, text='hon_3280k')
    dp.register_callback_query_handler(pr_hon_6480k, text='hon_6480k')

    dp.register_callback_query_handler(pr_hon_buy_sp, text='buy_hon_sp')
    dp.register_callback_query_handler(pr_hon_buy_60k, text='buy_hon_60k')
    dp.register_callback_query_handler(pr_hon_buy_300k, text='buy_hon_300k')
    dp.register_callback_query_handler(pr_hon_buy_980k, text='buy_hon_980k')
    dp.register_callback_query_handler(pr_hon_buy_1980k, text='buy_hon_1980k')
    dp.register_callback_query_handler(pr_hon_buy_3280k, text='buy_hon_3280k')
    dp.register_callback_query_handler(pr_hon_buy_6480k, text='buy_hon_6480k')
