from aiogram import types
from app import keyboards as kb
from app.var import bot, dp, check_sub_channel, NEWS_ID, show_item_prev_buy, confirm_item_buy
from app import database as db

from dotenv import load_dotenv
import os

load_dotenv()
op_id = os.getenv('OPERATOR_ID')


async def ds_decorations_fantasy(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(text='Discord Украшения Fantasy.\nВыберите категорию:',
                                        chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=kb.keyboard_discord_decorations_fantasy)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def ds_decorations_fantasy_avatar(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(text='🔮Discord Украшения аватара Fantasy.\nВыберите категорию:',
                                        chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=kb.keyboard_discord_decorations_fantasy_avatar)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def ds_decorations_fantasy_profile(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(text='🔮Discord Эффекты профиля Fantasy.\nВыберите категорию:',
                                        chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=kb.keyboard_discord_decorations_fantasy_profile)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def ds_decorations_anime(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(text='Discord Украшения Anime.\nВыберите категорию:',
                                        chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=kb.keyboard_discord_decorations_anime)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def ds_decorations_anime_avatar(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(text='✨Discord Украшения аватара Anime.\nВыберите категорию:',
                                        chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=kb.keyboard_discord_decorations_anime_avatar)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def ds_decorations_anime_profile(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(text='✨Discord Эффекты профиля Anime.\nВыберите категорию:',
                                        chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=kb.keyboard_discord_decorations_anime_profile)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def ds_decorations_breakfast(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(text='Discord Украшения Breakfast.\nВыберите категорию:',
                                        chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=kb.keyboard_discord_decorations_breakfast)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def ds_decorations_breakfast_avatar(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(text='🥐Discord Украшения аватара Breakfast.\nВыберите категорию:',
                                        chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=kb.keyboard_discord_decorations_breakfast_avatar)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


async def ds_decorations_breakfast_profile(callback_query: types.CallbackQuery):
    blocked_raw = (await db.show_blocked_users())
    blocked = list(map(lambda user: user[0], blocked_raw))
    if callback_query.from_user.id not in blocked:
        if await check_sub_channel(
                await bot.get_chat_member(chat_id=f'@{NEWS_ID}', user_id=callback_query.from_user.id)):
            await db.set_active(callback_query.from_user.id, 1)
            await bot.edit_message_text(text='🥐Discord Эффекты профиля Breakfast.\nВыберите категорию:',
                                        chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=kb.keyboard_discord_decorations_breakfast_profile)
        else:
            await callback_query.message.answer(
                f'''Для доступа к функционалу магазина, сначала подпишитесь на наш <a href='https://t.me/{NEWS_ID}'>канал</a>.''',
                parse_mode=types.ParseMode.HTML)
            await db.set_active(callback_query.from_user.id, 0)
    else:
        await db.set_active(callback_query.from_user.id, 0)


def reg_hand_discord_decorations():
    dp.register_callback_query_handler(ds_decorations_fantasy, text='discord_fantasy')
    dp.register_callback_query_handler(ds_decorations_fantasy, text='discord_decorations_fantasy_anypiece_back')
    dp.register_callback_query_handler(ds_decorations_fantasy_avatar, text='discord_decorations_fantasy_avatar')
    dp.register_callback_query_handler(ds_decorations_fantasy_profile, text='discord_decorations_fantasy_profile')
    dp.register_callback_query_handler(ds_decorations_fantasy_profile,
                                       text='discord_decorations_fantasy_profile_any_back')
    dp.register_callback_query_handler(ds_decorations_fantasy_avatar,
                                       text='discord_decorations_fantasy_avatar_any_back')
    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_fantasy_avatar', 'Discord Пылающий меч',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fantasy-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_fantasy_avatar_1_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_fantasy_avatar_1')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_fantasy_avatar', 'Discord Пылающий меч',
                                                                  callback_query=q),
                                       text='discord_decorations_fantasy_avatar_1_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_fantasy_avatar', 'Discord Волшебное зелье',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fantasy-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_fantasy_avatar_2_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_fantasy_avatar_2')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_fantasy_avatar', 'Discord Волшебное зелье',
                                                                  callback_query=q),
                                       text='discord_decorations_fantasy_avatar_2_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_fantasy_avatar', 'Discord Феи',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fantasy-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_fantasy_avatar_3_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_fantasy_avatar_3')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_fantasy_avatar', 'Discord Феи',
                                                                  callback_query=q),
                                       text='discord_decorations_fantasy_avatar_3_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_fantasy_avatar', 'Discord Посох волшебника',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fantasy-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_fantasy_avatar_4_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_fantasy_avatar_4')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_fantasy_avatar', 'Discord Посох волшебника',
                                                                  callback_query=q),
                                       text='discord_decorations_fantasy_avatar_4_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_fantasy_avatar', 'Discord Светящиеся руны',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fantasy-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_fantasy_avatar_5_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_fantasy_avatar_5')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_fantasy_avatar', 'Discord Светящиеся руны',
                                                                  callback_query=q),
                                       text='discord_decorations_fantasy_avatar_5_buy')

    dp.register_callback_query_handler(
        lambda q: show_item_prev_buy('ds_dec_fantasy_avatar', 'Discord Оборонительный щит',
                                     "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fantasy-11-20'>*Тык*</a>",
                                     kb.keyboard_discord_decorations_fantasy_avatar_6_buy,
                                     callback_query=q),
        text='discord_decorations_fantasy_avatar_6')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_fantasy_avatar', 'Discord Оборонительный щит',
                                                                  callback_query=q),
                                       text='discord_decorations_fantasy_avatar_6_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_fantasy_avatar', 'Discord Медальон-череп',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fantasy-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_fantasy_avatar_7_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_fantasy_avatar_7')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_fantasy_avatar', 'Discord Медальон-череп',
                                                                  callback_query=q),
                                       text='discord_decorations_fantasy_avatar_7_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_fantasy_avatar', 'Discord Сокровище и ключ',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fantasy-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_fantasy_avatar_8_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_fantasy_avatar_8')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_fantasy_avatar', 'Discord Медальон-череп',
                                                                  callback_query=q),
                                       text='discord_decorations_fantasy_avatar_8_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_fantasy_profile', 'Discord Водяной заряд',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fantasy-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_fantasy_profile_1_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_fantasy_profile_1')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_fantasy_profile', 'Discord Водяной заряд',
                                                                  callback_query=q),
                                       text='discord_decorations_fantasy_profile_1_buy')

    dp.register_callback_query_handler(
        lambda q: show_item_prev_buy('ds_dec_fantasy_profile', 'Discord Безмятежная сакура',
                                     "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fantasy-11-20'>*Тык*</a>",
                                     kb.keyboard_discord_decorations_fantasy_profile_2_buy,
                                     callback_query=q),
        text='discord_decorations_fantasy_profile_2')

    dp.register_callback_query_handler(
        lambda q: confirm_item_buy('ds_dec_fantasy_profile', 'Discord Безмятежная сакура',
                                   callback_query=q),
        text='discord_decorations_fantasy_profile_2_buy')

    dp.register_callback_query_handler(
        lambda q: show_item_prev_buy('ds_dec_fantasy_profile', 'Discord Таинственные лозы',
                                     "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fantasy-11-20'>*Тык*</a>",
                                     kb.keyboard_discord_decorations_fantasy_profile_3_buy,
                                     callback_query=q),
        text='discord_decorations_fantasy_profile_3')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_fantasy_profile', 'Discord Таинственные лозы',
                                                                  callback_query=q),
                                       text='discord_decorations_fantasy_profile_3_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_fantasy_profile', 'Discord Пыльца пикси',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Fantasy-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_fantasy_profile_4_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_fantasy_profile_4')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_fantasy_profile', 'Discord Пыльца пикси',
                                                                  callback_query=q),
                                       text='discord_decorations_fantasy_profile_4_buy')

    dp.register_callback_query_handler(ds_decorations_anime, text='discord_anime')
    dp.register_callback_query_handler(ds_decorations_anime, text='discord_decorations_anime_anypiece_back')
    dp.register_callback_query_handler(ds_decorations_anime_avatar, text='discord_decorations_anime_avatar')
    dp.register_callback_query_handler(ds_decorations_anime_profile, text='discord_decorations_anime_profile')
    dp.register_callback_query_handler(ds_decorations_anime_profile,
                                       text='discord_decorations_anime_profile_any_back')
    dp.register_callback_query_handler(ds_decorations_anime_avatar,
                                       text='discord_decorations_anime_avatar_any_back')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_anime_avatar', 'Discord Излучая энергию',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Anime-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_anime_avatar_1_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_anime_avatar_1')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_anime_avatar', 'Discord Излучая энергию',
                                                                  callback_query=q),
                                       text='discord_decorations_anime_avatar_1_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_anime_avatar', 'Discord Душа покидает тело',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Anime-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_anime_avatar_2_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_anime_avatar_2')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_anime_avatar', 'Discord Душа покидает тело',
                                                                  callback_query=q),
                                       text='discord_decorations_anime_avatar_2_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_anime_avatar', 'Discord Пот градом',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Anime-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_anime_avatar_3_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_anime_avatar_3')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_anime_avatar', 'Discord Пот градом',
                                                                  callback_query=q),
                                       text='discord_decorations_anime_avatar_3_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_anime_avatar', 'Discord В мечтах',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Anime-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_anime_avatar_4_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_anime_avatar_4')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_anime_avatar', 'Discord В мечтах',
                                                                  callback_query=q),
                                       text='discord_decorations_anime_avatar_4_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_anime_avatar', 'Discord Пришла любовь',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Anime-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_anime_avatar_5_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_anime_avatar_5')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_anime_avatar', 'Discord Пришла любовь',
                                                                  callback_query=q),
                                       text='discord_decorations_anime_avatar_5_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_anime_avatar', 'Discord В шоке',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Anime-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_anime_avatar_6_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_anime_avatar_6')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_anime_avatar', 'Discord В шоке',
                                                                  callback_query=q),
                                       text='discord_decorations_anime_avatar_6_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_anime_avatar', 'Discord Гнев',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Anime-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_anime_avatar_7_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_anime_avatar_7')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_anime_avatar', 'Discord Гнев',
                                                                  callback_query=q),
                                       text='discord_decorations_anime_avatar_7_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_anime_profile', 'Discord Волшебные сердца',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Anime-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_anime_profile_1_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_anime_profile_1')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_fantasy_profile', 'Discord Волшебные сердца',
                                                                  callback_query=q),
                                       text='discord_decorations_anime_profile_1_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_anime_profile', 'Discord Осколок',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Anime-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_anime_profile_2_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_anime_profile_2')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_fantasy_profile', 'Discord Осколок',
                                                                  callback_query=q),
                                       text='discord_decorations_anime_profile_2_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_anime_profile', 'Discord Бросок сюрикена',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Anime-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_anime_profile_3_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_anime_profile_3')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_fantasy_profile', 'Discord Бросок сюрикена',
                                                                  callback_query=q),
                                       text='discord_decorations_anime_profile_3_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_anime_profile', 'Discord Пиковая мощность',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Anime-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_anime_profile_4_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_anime_profile_4')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_fantasy_profile', 'Discord Пиковая мощность',
                                                                  callback_query=q),
                                       text='discord_decorations_anime_profile_4_buy')

    dp.register_callback_query_handler(ds_decorations_breakfast, text='discord_breakfast')
    dp.register_callback_query_handler(ds_decorations_breakfast, text='discord_decorations_breakfast_anypiece_back')
    dp.register_callback_query_handler(ds_decorations_breakfast_avatar, text='discord_decorations_breakfast_avatar')
    dp.register_callback_query_handler(ds_decorations_breakfast_profile, text='discord_decorations_breakfast_profile')
    dp.register_callback_query_handler(ds_decorations_breakfast_profile,
                                       text='discord_decorations_breakfast_profile_any_back')
    dp.register_callback_query_handler(ds_decorations_breakfast_avatar,
                                       text='discord_decorations_breakfast_avatar_any_back')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_breakfast_avatar', 'Discord Тост',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Breakfast-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_breakfast_avatar_1_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_breakfast_avatar_1')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_breakfast_avatar', 'Discord Тост',
                                                                  callback_query=q),
                                       text='discord_decorations_breakfast_avatar_1_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_breakfast_avatar', 'Discord Утренний кофе',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Breakfast-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_breakfast_avatar_2_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_breakfast_avatar_2')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_breakfast_avatar', 'Discord Утренний кофе',
                                                                  callback_query=q),
                                       text='discord_decorations_breakfast_avatar_2_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_breakfast_avatar', 'Discord Жаренное яйцо',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Breakfast-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_breakfast_avatar_3_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_breakfast_avatar_3')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_breakfast_avatar', 'Discord Жаренное яйцо',
                                                                  callback_query=q),
                                       text='discord_decorations_breakfast_avatar_3_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_breakfast_avatar', 'Discord Черничный джем',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Breakfast-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_breakfast_avatar_4_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_breakfast_avatar_4')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_breakfast_avatar', 'Discord Черничный джем',
                                                                  callback_query=q),
                                       text='discord_decorations_breakfast_avatar_4_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_breakfast_avatar', 'Discord Пончик',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Breakfast-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_breakfast_avatar_5_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_breakfast_avatar_5')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_breakfast_avatar', 'Discord Пончик',
                                                                  callback_query=q),
                                       text='discord_decorations_breakfast_avatar_5_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_breakfast_avatar', 'Discord Оладушки',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Breakfast-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_breakfast_avatar_6_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_breakfast_avatar_6')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_breakfast_avatar', 'Discord Оладушки',
                                                                  callback_query=q),
                                       text='discord_decorations_breakfast_avatar_6_buy')

    dp.register_callback_query_handler(lambda q: show_item_prev_buy('ds_dec_breakfast_profile', 'Discord Discord-Os',
                                                                    "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Breakfast-11-20'>*Тык*</a>",
                                                                    kb.keyboard_discord_decorations_breakfast_profile_1_buy,
                                                                    callback_query=q),
                                       text='discord_decorations_breakfast_profile_1')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_breakfast_profile', 'Discord Discord-Os',
                                                                  callback_query=q),
                                       text='discord_decorations_breakfast_profile_1_buy')

    dp.register_callback_query_handler(
        lambda q: show_item_prev_buy('ds_dec_breakfast_profile', 'Discord Сытный завтрак',
                                     "<a href='https://telegra.ph/Magazin-Discord-Kollekciya-Breakfast-11-20'>*Тык*</a>",
                                     kb.keyboard_discord_decorations_breakfast_profile_2_buy,
                                     callback_query=q),
        text='discord_decorations_breakfast_profile_2')

    dp.register_callback_query_handler(lambda q: confirm_item_buy('ds_dec_breakfast_profile', 'Discord Сытный завтрак',
                                                                  callback_query=q),
                                       text='discord_decorations_breakfast_profile_2_buy')
