import aiogram.utils.exceptions
from aiogram import types
from aiogram.utils import executor
from aiogram.types.message import ContentType, ParseMode

import os

from app import keyboards as kb
from app import database as db
from app.var import dp, bot, check_sub_channel, NEWS_ID, REVIEWS_ID

from handlers.profile_hnd import reg_hand_profile
from handlers.admin_hnd import reg_hand_admin
from handlers.discord_hnd import reg_hand_discord
from handlers.genshin_hnd import reg_hand_genshin
from handlers.honkai_hnd import reg_hand_honkai
from handlers.tg_hnd import reg_hand_tg
from handlers.yand_hnd import reg_hand_ya
from handlers.xbox_hnd import reg_hand_xbox
from handlers.other_hnd import reg_hand_other

from dotenv import load_dotenv

load_dotenv()
adm_id = int(os.getenv('ADMIN_ID'))


async def on_startup(_):
    await db.db_start()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if message.chat.type == 'private':
            if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=message.from_user.id)):
                await db.set_active(message.from_user.id, 1)
                z = await db.cmd_start_db(message.from_user.id)
                await message.answer(
                    f'''
Привет, {message.from_user.first_name}!
Добро пожаловать в магазин

<a href='https://t.me/asurastore_news'>Новости</a> | <a href='https://t.me/asurastore_reviews'>Отзывы</a>''',

                    reply_markup=kb.keyboard_main, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
                if z:
                    await bot.send_message(adm_id,
                                           f'Новый пользователь: {message.from_user.full_name}\n@{message.from_user.username}\n\nВсего пользователей:{z}')
                if message.from_user.id == adm_id:
                    await message.answer(f"Вы авторизовались как администратор, {message.from_user.full_name}",
                                         reply_markup=kb.keyboard_main_admin)
            else:
                await message.answer(
                    f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
                await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                await message.reply("Техническая поддержка магазина: @AsuraStore_helper")
        else:
            await message.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.message_handler(text='Помощь')
async def process_help_command(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                await message.reply("Техническая поддержка магазина: @AsuraStore_helper")
        else:
            await message.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.message_handler(text='Руководство')
async def process_help_command(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                await message.reply(
                    "Нажмите на кнопку 'Товары', выберите интересующую вас категорию и вид товара, после чего следуйте инструкции")
        else:
            await message.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.message_handler(text='Товары')
async def stock_message(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                await message.answer("Доступные категории в магазине:",
                                     reply_markup=kb.keyboard_stock_inl)
        else:
            await message.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.message_handler(commands=['review'])
async def addreview(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            text = message.text[8:]
            try:
                pr = await db.show_last_purchase_id(message.from_user.id)

                await bot.send_message(chat_id=REVIEWS_ID,
                                       text=f'''Номер заказа {pr[0]}\nВремя заказа: {pr[1].split('.')[0]}\nТип товара: {pr[2]}\n\nПользователь: @{message.from_user.username}\n{text}''')
            except TypeError:
                await message.answer('Вы не совершили ни одной покупки')
        else:
            await message.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.message_handler(commands=['useractive'])
async def show_active_comand(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=message.from_user.id)):
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
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.message_handler(commands=['sendall'])
async def sendall(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda userz: userz[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=message.from_user.id)):
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
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.message_handler(commands=['addmn'])
async def sendall(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                if message.from_user.id == adm_id:
                    text = message.text[7:]
                    id_us = text.split(' ')[0]
                    mn = text.split(' ')[1]
                    if await db.user_exists(id_us):
                        if await db.user_is_active(id_us) and await check_sub_channel(
                                await bot.get_chat_member(chat_id=NEWS_ID, user_id=id_us)):
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
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.message_handler(commands=['cgprice'])
async def priceadmn(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=message.from_user.id)):
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
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.message_handler(commands=['list_blocked'])
async def pr_block_list_comm(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.from_user.id == adm_id:
                await message.answer(f'Заблокированные пользователи: {blocked}')
            else:
                await message.reply(
                    'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
        else:
            await message.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.message_handler(commands=['block'])
async def pr_block_command(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.from_user.id == adm_id:
                id_us = message.text[7:]
                if await db.user_exists(id_us):
                    await db.set_block_user_status(id_us, 1)
                    await message.answer(f'Пользователь {id_us} заблокирован')
                else:
                    await message.answer(f'Пользователь {id_us} не зарегистрирован')
            else:
                await message.reply(
                    'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
        else:
            await message.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.message_handler(commands=['unblock'])
async def pr_block_command(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=message.from_user.id)):
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
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(message.from_user.id, 0)


reg_hand_profile()
reg_hand_admin()
reg_hand_discord()
reg_hand_genshin()
reg_hand_honkai()
reg_hand_tg()
reg_hand_ya()
reg_hand_xbox()
reg_hand_other()


@dp.message_handler()
async def echo_message(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            await message.reply(
                'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
        else:
            await message.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(message.from_user.id, 0)


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=message.from_user.id)):
            await message.reply(
                'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
        else:
            await message.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(message.from_user.id, 0)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
