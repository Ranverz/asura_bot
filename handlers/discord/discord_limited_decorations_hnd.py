from aiogram import types
from app import keyboards as kb
from app.var import bot, dp, check_sub_channel, NEWS_ID, show_item_prev_buy, confirm_item_buy
from app import database as db

from dotenv import load_dotenv
import os

load_dotenv()
op_id = os.getenv('OPERATOR_ID')


async def ds_decorations_limited(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(text='🍂Discord Украшения Fall.\nВыберите категорию:',
                                        chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=kb.keyboard_discord_decorations_limited)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def ds_decorations_limited_avatar(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(text='🍂Discord Украшения аватара Fall.\nВыберите категорию:',
                                        chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=kb.keyboard_discord_decorations_limited_avatar)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def ds_decorations_limited_profile(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(text='🍂Discord Эффекты профиля Fall.\nВыберите категорию:',
                                        chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=kb.keyboard_discord_decorations_limited_profile)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


def reg_hand_discord_limited_decorations():
    dp.register_callback_query_handler(ds_decorations_limited, text='discord_limited')
    dp.register_callback_query_handler(ds_decorations_limited, text='discord_decorations_limited_anypiece_back')
    dp.register_callback_query_handler(ds_decorations_limited_avatar, text='discord_decorations_limited_avatar')
    dp.register_callback_query_handler(ds_decorations_limited_profile, text='discord_decorations_limited_profile')
    dp.register_callback_query_handler(ds_decorations_limited_profile,
                                       text='discord_decorations_limited_profile_any_back')
    dp.register_callback_query_handler(ds_decorations_limited_avatar,
                                       text='discord_decorations_limited_avatar_any_back')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_limited_profile', 'Discord Обитатели пруда',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fall-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_limited_profile_1_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_limited_profile_1')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_limited_profile', 'Discord Обитатели пруда',
                                                                  callback_query=q),
                                       text='discord_decorations_limited_profile_1_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_limited_profile', 'Discord Золотая осень',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fall-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_limited_profile_2_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_limited_profile_2')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_limited_profile', 'Discord Золотая осень',
                                                                  callback_query=q),
                                       text='discord_decorations_limited_profile_2_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_limited_avatar', 'Discord Спелые тыквы',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fall-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_limited_avatar_1_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_limited_avatar_1')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_limited_avatar', 'Discord Спелые тыквы',
                                                                  callback_query=q),
                                       text='discord_decorations_limited_avatar_1_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_limited_avatar', 'Discord Шапка-лягушка',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fall-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_limited_avatar_2_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_limited_avatar_2')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_limited_avatar', 'Discord Шапка-лягушка',
                                                                  callback_query=q),
                                       text='discord_decorations_limited_avatar_2_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_limited_avatar', 'Discord Шапка-лиса',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fall-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_limited_avatar_3_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_limited_avatar_3')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_limited_avatar', 'Discord Шапка-лиса',
                                                                  callback_query=q),
                                       text='discord_decorations_limited_avatar_3_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_limited_avatar', 'Discord Осенние листья',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fall-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_limited_avatar_4_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_limited_avatar_4')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_limited_avatar', 'Discord Осенние листья',
                                                                  callback_query=q),
                                       text='discord_decorations_limited_avatar_4_buy')
