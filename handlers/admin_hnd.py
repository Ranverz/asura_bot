from aiogram import types
import aiogram.utils.exceptions
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import os
import datetime

from app import keyboards as kb
from app import database as db
from app.var import dp, check_sub_channel, NEWS_ID, bot, moscow_tz

from dotenv import load_dotenv

load_dotenv()
adm_id = int(os.getenv('ADMIN_ID'))
op_id = os.getenv('OPERATOR_ID')


# @dp.message_handler(text='Админ-панель')
async def show_admin_panel(message: types.Message):
    if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
        blocked_raw = (await db.show_blocked_users())
        blocked = list(map(lambda user: user[0], blocked_raw))
        if message.from_user.id not in blocked:
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                if message.from_user.id == int(os.getenv('ADMIN_ID')):
                    await message.answer(f'Вы вошли в админ-панель', reply_markup=kb.admin_panel)
                else:
                    await message.reply(
                        'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)


# @dp.message_handler(commands=['useractive'])
async def show_active_comand(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                if message.from_user.id == adm_id:
                    amm = len(await db.show_active_users())
                    amm_unactive = len(await db.show_unactive_users())
                    await message.reply(
                        f'''Всего активных пользователей(подписаны и не заблокировали): {amm}\nНеактивных: {amm_unactive}\n\nВсего: {amm + amm_unactive}''')
                else:
                    await message.reply(
                        'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')

        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


# @dp.message_handler(commands=['sendall'])
async def sendall_f(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda userz: userz[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                if message.from_user.id == adm_id:
                    text = message.text[9:]
                    users = await db.get_users()
                    for user in users:
                        try:
                            await bot.send_message(user[0], text)
                            if int(user[1]) != 1:
                                await db.set_active(user[0], 1)
                        except aiogram.utils.exceptions.BotBlocked:
                            await db.set_active(user[0], 0)

                    await message.answer('Успешная рассылка')
                else:
                    await message.reply(
                        'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


# @dp.message_handler(commands=['addmn'])
async def addmn_f(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                if message.from_user.id == adm_id:
                    text = message.text[7:]
                    id_us = text.split(' ')[0]
                    mn = text.split(' ')[1]
                    if await db.user_exists(id_us):
                        if await db.user_is_active(id_us) and await check_sub_channel(
                                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=id_us)):
                            try:
                                await bot.send_message(id_us, f'Ваш баланс пополнен на {mn}₽ админом')
                                await db.add_money(id_us, mn)
                                await message.answer(f'Успешно добавили {mn}₽ пользователю {id_us}')
                            except aiogram.exceptions.BotBlocked:
                                await message.answer(f'Пользователь {id_us} заблокировал бота, деньги не отправлены')
                                await db.set_active(id_us, 0)
                        else:
                            await message.answer(
                                f'Пользователь {id_us} не подписан на новостной канал, деньги не отправлены')
                    else:
                        await message.answer(
                            f'''Пользователь {id_us} не зарегистрирован в магазине, деньги не отправлены''')
                else:
                    await message.reply(
                        'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


# @dp.message_handler(commands=['cgprice'])
async def priceadmn(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.from_user.id == adm_id:
                text = message.text[9:]
                id_item = text.split(' ')[0]
                mn = text.split(' ')[1]
                await db.change_price(id_item, mn)
                await message.answer(f'Цена успешна для {id_item} успешно изменена на {mn}')

            else:
                await message.reply(
                    'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


# @dp.message_handler(commands=['list_blocked'])
async def pr_block_list_comm(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    txt = ''
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.from_user.id == adm_id:
                for i in blocked:
                    txt += f'<code>{i}</code>, '
                await message.answer(f'Заблокированные пользователи: {txt}\n\nВсего заблокировано: {len(blocked)}',
                                     parse_mode=types.ParseMode.HTML)
            else:
                await message.reply(
                    'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


# @dp.message_handler(commands=['block'])
async def pr_block_command(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.from_user.id == adm_id:
                id_us = message.text[7:]
                if await db.user_exists(id_us):
                    await db.set_block_user_status(id_us, 1)
                    await message.answer(f'Пользователь {id_us} заблокирован')
                    await db.set_active(id_us, 0)
                else:
                    await message.answer(f'Пользователь {id_us} не зарегистрирован')
            else:
                await message.reply(
                    'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


# @dp.message_handler(commands=['unblock'])
async def pr_unblock_command(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.from_user.id == adm_id:
                id_us = message.text[9:]
                if await db.user_exists(id_us):
                    await db.set_block_user_status(id_us, 0)
                    await message.answer(f'Пользователь {id_us} разблокирован')
                else:
                    await message.answer(f'Пользователь {id_us} не зарегистрирован')
            else:
                await message.reply(
                    'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


class NewCheck(StatesGroup):
    id_user_to_send = State()
    item_s = State()
    price_s = State()
    pay_confirm_s = State()
    test_st = State()


async def send_check_to_pay_initial(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            await NewCheck.id_user_to_send.set()
            if message.chat.type == 'private':
                if message.from_user.id == adm_id:
                    await message.answer(f'Введите id пользователя для отправки счёта')
                else:
                    await message.reply(
                        'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


async def send_check_to_pay_item_name(message: types.Message, state: FSMContext):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                if message.from_user.id == adm_id:
                    async with state.proxy() as data:
                        data['id_user_to_send'] = message.text
                    await message.answer(f'Введите название товара')
                    await NewCheck.next()
                else:
                    await message.reply(
                        'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


async def send_check_to_pay_item_price(message: types.Message, state: FSMContext):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                if message.from_user.id == adm_id:
                    async with state.proxy() as data:
                        data['item_s'] = message.text
                    await message.answer(f'Введите цену товара')
                    await NewCheck.next()
                else:
                    await message.reply(
                        'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


async def send_check_to_pay_last(message: types.Message, state: FSMContext):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                if message.from_user.id == adm_id:
                    async with state.proxy() as data:
                        data['price_s'] = int(message.text)
                        id_us = data['id_user_to_send']
                        item = data['item_s']
                        price = data['price_s']
                    if await db.user_exists(id_us):
                        if await db.user_is_active(id_us) and await check_sub_channel(
                                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=id_us)):
                            try:
                                await bot.send_message(id_us, f'''
Вам выставлен счёт:
Товар: {item}

💵 Цена: {price}₽''',
                                                       reply_markup=await kb.create_order(item, price))
                                await message.answer(f'''
Успешно отправили счёт пользователю {id_us}
Товар: {item}
Цена: {price}₽''')
                                await state.finish()
                            except aiogram.exceptions.BotBlocked:
                                await message.answer(f'Пользователь {id_us} заблокировал бота, счёт не отправлен')
                                await db.set_active(id_us, 0)
                        else:
                            await message.answer(
                                f'Пользователь {id_us} не подписан на новостной канал, счёт не отправлен')
                    else:
                        await message.answer(
                            f'''Пользователь {id_us} не зарегистрирован в магазине, счёт не отправлен''')
                else:
                    await message.reply(
                        'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


async def confirm_check_paid(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            money = await db.show_money(callback_query.from_user.id)
            time = str(datetime.datetime.now(moscow_tz)).split('+')[0]

            data_prod_name_and_price = callback_query.values.get('data', '').split('!!')
            item_name = data_prod_name_and_price[1]  # Extracting the product name
            price = int(data_prod_name_and_price[2])

            if money >= price:
                await db.add_money(callback_query.from_user.id, -price)
                await db.add_purchase(callback_query.from_user.id, item_name, price, time)
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


async def cancel_paying_check(callback: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback.from_user.id)):
            await db.set_active(callback.from_user.id, 1)
            await bot.edit_message_text(text='Заказ отменен', chat_id=callback.message.chat.id,
                                        message_id=callback.message.message_id)
        else:
            await callback.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback.from_user.id, 0)
    else:
        await db.set_active(callback.from_user.id, 0)


def reg_hand_admin():
    dp.register_message_handler(show_admin_panel, text='Админ-панель')
    dp.register_message_handler(show_active_comand, commands=['useractive'])
    dp.register_message_handler(sendall_f, commands=['sendall'])
    dp.register_message_handler(addmn_f, commands=['addmn'])
    dp.register_message_handler(priceadmn, commands=['cgprice'])
    dp.register_message_handler(pr_block_list_comm, commands=['list_blocked'])
    dp.register_message_handler(pr_block_command, commands=['block'])
    dp.register_message_handler(pr_unblock_command, commands=['unblock'])
    dp.register_message_handler(send_check_to_pay_initial, commands=['send_check'])
    dp.register_message_handler(send_check_to_pay_item_name, state=NewCheck.id_user_to_send)
    dp.register_message_handler(send_check_to_pay_item_price, state=NewCheck.item_s)
    dp.register_message_handler(send_check_to_pay_last, state=NewCheck.price_s)
    dp.register_callback_query_handler(confirm_check_paid, text_contains='custom_order_pay!!')
    dp.register_callback_query_handler(cancel_paying_check, text='custom_order_cancel')
