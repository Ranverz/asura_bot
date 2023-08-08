from aiogram import types
from aiogram.types import ParseMode

from app.var import bot, dp, check_sub_channel, NEWS_ID
from app import database as db
from app import keyboards as kb

from dotenv import load_dotenv
import os

load_dotenv()
op_id = os.getenv('OPERATOR_ID')


# @dp.callback_query_handler(text='btnotherserv')
async def process_callback_button_other_s(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(
                text='Для покупки цифровых товаров, не находящихся в ассортименте напишите @AsuraStore_helper, с названием товара, который вы хотели бы купить.\n(доступны <code>PS Store</code>, <code>Chatgpt</code>, <code>Netflix</code>, <code>Youtube premium</code>, <code>Patreon</code> и многие другие, просто напишите свое пожелание и по возможности мы купим вам то, в чем вы нуждаетесь)',
                reply_markup=kb.keyboard_other_back, parse_mode=ParseMode.HTML, chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def pr_other_back_btn(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(text='Доступные категории в магазине:',
                                        reply_markup=kb.keyboard_stock_inl, chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


def reg_hand_other():
    dp.register_callback_query_handler(process_callback_button_other_s, text='btnotherserv')
    dp.register_callback_query_handler(pr_other_back_btn, text='buy_other_back')
