from aiogram import types
from aiogram.utils import executor
from aiogram.types.message import ContentType, ParseMode
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

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


class Newreviewm(StatesGroup):
    id_pr_mark = State()
    rev_mark = State()
    rev_confirm = State()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if message.chat.type == 'private':
            if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
                await db.set_active(message.from_user.id, 1)
                z = await db.cmd_start_db(message.from_user.id)
                await message.answer(
                    f'''
Привет, {message.from_user.first_name}!
Добро пожаловать в магазин

<a href='https://t.me/{NEWS_ID}'>Новости</a> | <a href='https://t.me/{REVIEWS_ID}'>Отзывы</a>''',

                    reply_markup=kb.keyboard_main, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
                if z:
                    await bot.send_message(adm_id,
                                           f'Новый пользователь: {message.from_user.full_name}\n@{message.from_user.username}\n\nВсего пользователей:{z}')
                if message.from_user.id == adm_id:
                    await message.answer(f"Вы авторизовались как администратор, {message.from_user.full_name}",
                                         reply_markup=kb.keyboard_main_admin)
            else:
                await message.answer(
                    f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                    parse_mode=types.ParseMode.HTML)
                await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                await message.reply("Техническая поддержка магазина: @AsuraStore_helper")
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.message_handler(text='Помощь')
async def process_help_command(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                await message.reply("Техническая поддержка магазина: @AsuraStore_helper")
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.message_handler(text='Руководство')
async def process_help_command(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                await message.reply(
                    "Нажмите на кнопку 'Товары', выберите интересующую вас категорию и вид товара, после чего следуйте инструкции")
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.message_handler(text='Товары')
async def stock_message(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                await message.answer("Доступные категории в магазине:",
                                     reply_markup=kb.keyboard_stock_inl)
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.callback_query_handler(text_contains='addreview_')
async def addreview_activate_fsm(callback: types.CallbackQuery, state: FSMContext):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback.from_user.id)):
            await db.set_active(callback.from_user.id, 1)
            await Newreviewm.id_pr_mark.set()
            id_pr_for_rev = callback.message.reply_markup.inline_keyboard[0][0].callback_data.split('_')[1]
            async with state.proxy() as data:
                data['id_pr_mark'] = id_pr_for_rev
            await callback.message.answer(f'Выберите оценку для заказа номер {id_pr_for_rev}',
                                          reply_markup=kb.keyboard_review_mark)
            await Newreviewm.next()
        else:
            await callback.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback.from_user.id, 0)
    else:
        await db.set_active(callback.from_user.id, 0)


@dp.message_handler(content_types=['text'], state=Newreviewm.rev_mark)
async def addreview_mark(message: types.Message, state: FSMContext):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                txt = message.text
                async with state.proxy() as data:
                    if txt == '❤️' or txt == '👎':
                        data['rev_mark'] = txt
                        await Newreviewm.next()
                        await message.answer('''Введите текст отзыва.
                        
Пример:
Отличный магазин. Все сделали быстро.''', reply_markup=kb.keyboard_review_text_empty)
                    elif txt == 'Не оставлять отзыв':
                        await state.finish()
                        await message.answer('Ваш отзыв отменен.', reply_markup=kb.keyboard_main)
                    else:
                        await message.answer('Выберите оценку из меню снизу.')
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.callback_query_handler(text='review_notext', state=Newreviewm.rev_confirm)
async def addreview_notext(callback: types.CallbackQuery, state: FSMContext):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback.from_user.id)):
            await db.set_active(callback.from_user.id, 1)
            async with state.proxy() as data:
                mr = data['rev_mark']
                id_pr = data['id_pr_mark']
            pr = await db.show_purchase_info(callback.from_user.id, id_pr)
            await bot.send_message(chat_id=f'@{REVIEWS_ID}', text=f'''
Номер заказа: {id_pr}
Время заказа: {pr[0]}
Тип товара: {pr[1]}

Пользователь: @{callback.from_user.username}
Оценка: {mr}
Отзыв: [Пользователь решил не оставлять текст.]''')
            await callback.message.answer('Ваш отзыв опубликован, без текста', reply_markup=kb.keyboard_main)
            await state.finish()
        else:
            await callback.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback.from_user.id, 0)
    else:
        await db.set_active(callback.from_user.id, 0)


@dp.message_handler(content_types=['text'], state=Newreviewm.rev_confirm)
async def addreview_text(message: types.Message, state: FSMContext):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            if message.chat.type == 'private':
                txt = message.text
                if txt != '':
                    async with state.proxy() as data:
                        mr = data['rev_mark']
                        id_pr = data['id_pr_mark']
                    pr = await db.show_purchase_info(message.from_user.id, id_pr)
                    await bot.send_message(chat_id=f'@{REVIEWS_ID}',
                                           text=f'''
Номер заказа: {id_pr}
Время заказа: {pr[0]}
Тип товара: {pr[1]}

Пользователь: @{message.from_user.username}
Оценка: {mr}
Отзыв: {txt}''')

                    await message.answer('Ваш отзыв опубликован', reply_markup=kb.keyboard_main)
                    await state.finish()
                else:
                    await message.answer('''Введите текст отзыва.
                        
Пример:
Отличный магазин. Все сделали быстро.''')
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
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
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await db.set_active(message.from_user.id, 1)
            await message.reply(
                'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(message: types.Message):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if message.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=message.from_user.id)):
            await message.reply(
                'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
        else:
            await message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(message.from_user.id, 0)
    else:
        await db.set_active(message.from_user.id, 0)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
