import datetime
import os
import aiofiles
from math import ceil

import aiogram.utils.exceptions
from aiogram.types import ParseMode
from yoomoney import Quickpay, Client

from app.var import dp, bot, check_sub_channel, NEWS_ID
from app import database as db
from aiogram import types

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from app import keyboards as kb

from dotenv import load_dotenv

load_dotenv()
client = Client(os.getenv('YM_API_TOKEN'))


class NewOrder(StatesGroup):
    amount = State()
    pay = State()


# @dp.message_handler(text='Профиль')
async def process_profile_command(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                # Retrieve user information from dp.data dictionary
                profile = await db.show_profile(message.from_user.id)
                reg_date = profile[2]
                balance = profile[3]
                bought_items = profile[4]

                await message.answer(
                    f'''Профиль
Имя: {message.from_user.first_name}
Логин: @{message.from_user.username}
ID: <code>{message.from_user.id}</code>
Дата регистрации: {reg_date}

Баланс: {balance}₽
Количество покупок: {bought_items}''',
                    reply_markup=kb.keyboard_profile, parse_mode=ParseMode.HTML
                )
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


# @dp.callback_query_handler(text='profile_history')
async def show_purchased_history(call: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if call.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=call.from_user.id)):
            await db.set_active(call.from_user.id, 1)
            formatted_ans = ''
            profile = await db.show_history(call.from_user.id)
            if len(profile) != 0:
                for c in profile:
                    formatted_ans += f"Номер покупки: {c[0]}\nТовар: {c[2]}\nЦена: {c[3]}₽\nДата покупки(гг-мм-дд): {c[4].split('.')[0]}\n\n"
                try:
                    await call.message.answer(formatted_ans)
                except aiogram.utils.exceptions.MessageIsTooLong:
                    async with aiofiles.open(f'purchase_list_for_{call.from_user.id}.txt', 'w',
                                             encoding='utf-8') as file:
                        await file.write(formatted_ans)
                    document = types.input_file.InputFile(f'purchase_list_for_{call.from_user.id}.txt')
                    await bot.send_document(chat_id=call.message.chat.id, document=document)
                    os.remove(f'purchase_list_for_{call.from_user.id}.txt')
            else:
                await call.answer(text='Вы не совершили ни одной покупки', show_alert=True)
        else:
            await call.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(call.from_user.id, 0)
    else:
        await db.set_active(call.from_user.id, 0)


# @dp.callback_query_handler(text='profile_insert')
async def top_up(callback: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback.from_user.id)):
            await db.set_active(callback.from_user.id, 1)
            # await bot.delete_message(callback.from_user.id, callback.message.message_id)
            await NewOrder.amount.set()
            await bot.send_message(callback.from_user.id,
                                   f'''
Введите сумму для пополнения, минимальная сумма - 5 рублей
<code>Для пополнения по номеру карты(сбербанк, тинькофф) напишите в личные сообщения @AsuraStore_helper.</code>
    
Через платежную систему(Юмани) комиссия 3% с банковских карт, с баланса Юмани комиссии нет. 
    ''',
                                   reply_markup=kb.choose_insert, parse_mode=types.ParseMode.HTML)
        else:
            await callback.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback.from_user.id, 0)
    else:
        await db.set_active(callback.from_user.id, 0)


async def cancel_choosing_payment(callback: types.CallbackQuery, state: FSMContext):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback.from_user.id)):
            await db.set_active(callback.from_user.id, 1)
            curr_state = await state.get_state()
            if curr_state is None:
                return
            await state.finish()
            await callback.message.delete()
            await callback.message.answer("Пополнение отменено")
        else:
            await callback.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback.from_user.id, 0)
    else:
        await db.set_active(callback.from_user.id, 0)


# @dp.callback_query_handler(text='cancel_insert', state=*)
async def cancel_p(callback: types.CallbackQuery, state: FSMContext):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback.from_user.id)):
            await db.set_active(callback.from_user.id, 1)
            curr_state = await state.get_state()
            if curr_state is None:
                return
            await state.finish()
            await callback.message.delete()
            await callback.message.answer('Оплата отменена')
        else:
            await callback.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback.from_user.id, 0)
    else:
        await db.set_active(callback.from_user.id, 0)


# @dp.message_handler(content_types=['text'], state=NewOrder.amount)
async def create_p(message: types.Message, state: FSMContext):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                async with state.proxy() as data:
                    if message.text.isnumeric() and int(message.text) >= 5:
                        data['amount'] = int(message.text)
                        comment = f'{message.from_user.id}.{datetime.datetime.now()}'
                    else:
                        await message.answer(
                            '''
Введите сумму для пополнения, минимальная сумма - 5 рублей.
Сумма пополнения должна быть целым числом без копеек.
    
Чтобы отменить пополнение или использовать другой функционал бота нажмите кнопку "Отмена"''',
                            reply_markup=kb.choose_insert)

                quickpay = Quickpay(
                    receiver="4100118098927795",
                    quickpay_form="shop",
                    targets="Sponsor this project",
                    paymentType="SB",
                    sum=data['amount'] / 0.97,
                    label=comment,
                )

                await bot.send_message(message.from_user.id,
                                       f'''Оплатите {ceil(data['amount'] / 0.97 * 100) / 100}₽\nСсылка:{quickpay.redirected_url}''',
                                       reply_markup=kb.buy_menu(url=quickpay.redirected_url, bill=comment))
                await NewOrder.next()
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


# @dp.callback_query_handler(text_contains='check__')
async def check_pa(callback: types.CallbackQuery, state: FSMContext):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback.from_user.id)):
            await db.set_active(callback.from_user.id, 1)
            history = client.operation_history(label=callback.data[7:])

            try:
                stat = history.operations[0].status

                if stat == 'success':
                    async with state.proxy() as data:
                        amm = data['amount']
                    await state.finish()
                    await callback.message.delete()
                    await db.add_money(callback.from_user.id, amm)
                    await callback.message.answer(f'Ваш баланс успешно пополнен на <code>{amm}</code>₽',
                                                  parse_mode=types.ParseMode.HTML)

                else:
                    await callback.answer(text='Оплата не найдена', show_alert=True)

            except IndexError:
                await callback.answer(text='Оплата не найдена', show_alert=True)
        else:
            await callback.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback.from_user.id, 0)
    else:
        await db.set_active(callback.from_user.id, 0)


def reg_hand_profile():
    dp.register_message_handler(process_profile_command, text='Профиль')
    dp.register_callback_query_handler(show_purchased_history, text='profile_history')
    dp.register_callback_query_handler(cancel_choosing_payment, text='choose_insert_cancel', state=NewOrder.amount)
    dp.register_callback_query_handler(cancel_p, text='cancel_insert', state=NewOrder.pay)
    dp.register_callback_query_handler(top_up, text='profile_insert')
    dp.register_message_handler(create_p, state=NewOrder.amount)
    dp.register_callback_query_handler(check_pa, state=NewOrder.pay, text_contains='check__')
