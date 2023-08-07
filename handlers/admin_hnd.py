from aiogram import types
import aiogram.utils.exceptions
import os

from app import keyboards as kb
from app import database as db
from app.var import dp, check_sub_channel, NEWS_ID, bot

from dotenv import load_dotenv

load_dotenv()
adm_id = int(os.getenv('ADMIN_ID'))


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
                                await db.set_active(message.from_user.id, 0)
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
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.from_user.id == adm_id:
                await message.answer(f'Заблокированные пользователи: {blocked}')
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


def reg_hand_admin():
    dp.register_message_handler(show_admin_panel, text='Админ-панель')
    dp.register_message_handler(show_active_comand, commands=['useractive'])
    dp.register_message_handler(sendall_f, commands=['sendall'])
    dp.register_message_handler(addmn_f, commands=['addmn'])
    dp.register_message_handler(priceadmn, commands=['cgprice'])
    dp.register_message_handler(pr_block_list_comm, commands=['list_blocked'])
    dp.register_message_handler(pr_block_command, commands=['block'])
    dp.register_message_handler(pr_unblock_command, commands=['unblock'])
