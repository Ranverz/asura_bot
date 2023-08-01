from aiogram import types

from app.var import bot, dp, check_sub_channel, NEWS_ID
from app import database as db

from dotenv import load_dotenv
import os

load_dotenv()
op_id = os.getenv('OPERATOR_ID')


# @dp.callback_query_handler(text='btnotherserv')
async def process_callback_button_other_s(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await callback_query.message.delete()
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text='Для покупки цифровых товаров, не находящихся в ассортименте напишите @AsuraStore_helper, с названием товара, который вы хотели бы купить.\n(доступны PS Store, Chatgpt, Netflix, Youtube premium, Patreon и многие другие, просто напишите свое пожелание и по возможности мы купим вам то, в чем вы нуждаетесь)')
        else:
            await callback_query.answer(
                f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
            await db.set_active(callback_query.from_user.id, 0)


def reg_hand_other():
    dp.register_callback_query_handler(process_callback_button_other_s, text='btnotherserv')
