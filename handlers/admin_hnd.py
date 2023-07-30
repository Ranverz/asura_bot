from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

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

# @dp.message_handler(text='Добавить товар')
# async def add_items(message: types.Message):
#     if message.from_user.id == int(os.getenv('ADMIN_ID')):
#         await NewOrder.item.set()
#         await message.answer(f"Выберите тип товара", reply_markup=kb.keyboard_stock_inl)
#     else:
#         await message.reply(
#             'К сожалению, я не могу распознать эту команду.\nВоспользуйтесь навигацией или командой /start')
#
#
# @dp.callback_query_handler(state=NewOrder.item)
# async def add_item_name(call: types.CallbackQuery, state: FSMContext):
#     async with state.proxy() as data:
#         data['item'] = call.data
#     await call.message.answer(f"Выберите тип товара", reply_markup=kb.keyboard_nitro)
#     await NewOrder.next()
#
#
# @dp.callback_query_handler(state=NewOrder.type)
# async def add_item_desc(call: types.CallbackQuery, state: FSMContext):
#     async with state.proxy() as data:
#         data['type'] = call.data
#     await call.message.answer(f"Напишите количество товара")
#     await NewOrder.next()
#
#
# @dp.message_handler(state=NewOrder.amount)
# async def add_item_price(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['amount'] = message.text
#     await message.answer(f"Отправьте фотографию товара")
#     await NewOrder.next()
#
#
# @dp.message_handler(lambda message: not message.photo, state=NewOrder.photo)
# async def add_item_photo_check(message: types.Message):
#     await message.answer('Это не фотография')
#
#
# @dp.message_handler(content_types=['photo'], state=NewOrder.photo)
# async def add_item_photo(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['photo'] = message.photo[0].file_id
#     await db.add_item(state)
#     await message.answer('Товар успешно создан', reply_markup=kb.admin_panel)
#     await state.finish()
