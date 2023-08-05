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
