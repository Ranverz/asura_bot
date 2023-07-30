from aiogram import types

import os

from app import keyboards as kb
from app import database as db
from app.var import dp, check_sub_channel, NEWS_ID, bot


# @dp.message_handler(text='Админ-панель')
async def show_admin_panel(message: types.Message):
    if await check_sub_channel(await bot.get_chat_member(chat_id=NEWS_ID, user_id=message.from_user.id)):
        await db.set_active(message.from_user.id, 1)
        if message.chat.type == 'private':
            if message.from_user.id == int(os.getenv('ADMIN_ID')):
                await message.answer(f'Вы вошли в админ-панель', reply_markup=kb.admin_panel)
            else:
                await message.reply(
                    'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
    else:
        await message.answer(
            f'Для доступа к функционалу магазина, сначала подпишитесь на наш канал.\nt.me/asurastore_news')
        await db.set_active(message.from_user.id, 0)


def reg_hand_admin():
    dp.register_message_handler(show_admin_panel, text='Админ-панель')
