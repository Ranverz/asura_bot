from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, WebAppInfo

keyboard_discord_decorations = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations.add(InlineKeyboardButton(text='🍂Fall', callback_data='discord_limited'),
                                 InlineKeyboardButton(text='🔮Fantasy', callback_data='discord_fantasy'),
                                 InlineKeyboardButton(text='✨Anime', callback_data='discord_anime'),
                                 InlineKeyboardButton(text='🥐Breakfast', callback_data='discord_breakfast'),
                                 InlineKeyboardButton(text='Назад', callback_data='discord_decorations_back'), )


async def create_order(item, price):
    keyboard_pay_custom_order = InlineKeyboardMarkup(row_width=1)
    keyboard_pay_custom_order.add(
        InlineKeyboardButton(text='Оплатить', callback_data=f'custom_order_pay!!{item}!!{price}'),
        InlineKeyboardButton(text='Отмена', callback_data='custom_order_cancel'))
    return keyboard_pay_custom_order


keyboard_discord_decorations_limited = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_limited.add(
    InlineKeyboardButton(text='🍂Украшения аватара', callback_data='discord_decorations_limited_avatar'),
    InlineKeyboardButton(text='🍂Эффекты профиля', callback_data='discord_decorations_limited_profile'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_anytheme_back'),
)

keyboard_discord_decorations_limited_avatar = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_limited_avatar.add(
    InlineKeyboardButton(text='🍂Спелые тыквы', callback_data='discord_decorations_limited_avatar_1'),
    InlineKeyboardButton(text='🍂Шапка-лягушка', callback_data='discord_decorations_limited_avatar_2'),
    InlineKeyboardButton(text='🍂Шапка-лиса', callback_data='discord_decorations_limited_avatar_3'),
    InlineKeyboardButton(text='🍂Осенние листья', callback_data='discord_decorations_limited_avatar_4'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_limited_anypiece_back'), )

keyboard_discord_decorations_limited_profile = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_limited_profile.add(
    InlineKeyboardButton(text='🍂Обитатели пруда', callback_data='discord_decorations_limited_profile_1'),
    InlineKeyboardButton(text='🍂Золотая осень', callback_data='discord_decorations_limited_profile_2'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_limited_anypiece_back'), )

keyboard_discord_decorations_limited_profile_1_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_limited_profile_1_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_limited_profile_1_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_limited_profile_any_back'), )

keyboard_discord_decorations_limited_profile_2_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_limited_profile_2_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_limited_profile_2_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_limited_profile_any_back'), )

keyboard_discord_decorations_limited_avatar_1_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_limited_avatar_1_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_limited_avatar_1_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_limited_avatar_any_back'), )

keyboard_discord_decorations_limited_avatar_2_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_limited_avatar_2_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_limited_avatar_2_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_limited_avatar_any_back'), )

keyboard_discord_decorations_limited_avatar_3_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_limited_avatar_3_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_limited_avatar_3_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_limited_avatar_any_back'), )

keyboard_discord_decorations_limited_avatar_4_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_limited_avatar_4_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_limited_avatar_4_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_limited_avatar_any_back'), )

keyboard_discord_decorations_fantasy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_fantasy.add(
    InlineKeyboardButton(text='🔮Украшения аватара', callback_data='discord_decorations_fantasy_avatar'),
    InlineKeyboardButton(text='🔮Эффекты профиля', callback_data='discord_decorations_fantasy_profile'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_anytheme_back'),
)

keyboard_discord_decorations_fantasy_avatar = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_fantasy_avatar.add(
    InlineKeyboardButton(text='🔮Пылающий меч', callback_data='discord_decorations_fantasy_avatar_1'),
    InlineKeyboardButton(text='🔮Волшебное зелье', callback_data='discord_decorations_fantasy_avatar_2'),
    InlineKeyboardButton(text='🔮Феи', callback_data='discord_decorations_fantasy_avatar_3'),
    InlineKeyboardButton(text='🔮Посох волшебника', callback_data='discord_decorations_fantasy_avatar_4'),
    InlineKeyboardButton(text='🔮Светящиеся руны', callback_data='discord_decorations_fantasy_avatar_5'),
    InlineKeyboardButton(text='🔮Оборонительный щит', callback_data='discord_decorations_fantasy_avatar_6'),
    InlineKeyboardButton(text='🔮Медальон-череп', callback_data='discord_decorations_fantasy_avatar_7'),
    InlineKeyboardButton(text='🔮Сокровище и ключ', callback_data='discord_decorations_fantasy_avatar_8'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_fantasy_anypiece_back'), )

keyboard_discord_decorations_fantasy_profile = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_fantasy_profile.add(
    InlineKeyboardButton(text='🔮Водяной заряд', callback_data='discord_decorations_fantasy_profile_1'),
    InlineKeyboardButton(text='🔮Безмятежная сакура', callback_data='discord_decorations_fantasy_profile_2'),
    InlineKeyboardButton(text='🔮Таинственные лозы', callback_data='discord_decorations_fantasy_profile_3'),
    InlineKeyboardButton(text='🔮Пыльца пикси', callback_data='discord_decorations_fantasy_profile_4'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_fantasy_anypiece_back'), )

keyboard_discord_decorations_fantasy_profile_1_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_fantasy_profile_1_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_fantasy_profile_1_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_fantasy_profile_any_back'), )

keyboard_discord_decorations_fantasy_profile_2_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_fantasy_profile_2_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_fantasy_profile_2_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_fantasy_profile_any_back'), )

keyboard_discord_decorations_fantasy_profile_3_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_fantasy_profile_3_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_fantasy_profile_3_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_fantasy_profile_any_back'), )

keyboard_discord_decorations_fantasy_profile_4_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_fantasy_profile_4_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_fantasy_profile_4_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_fantasy_profile_any_back'), )

keyboard_discord_decorations_fantasy_avatar_1_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_fantasy_avatar_1_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_fantasy_avatar_1_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_fantasy_avatar_any_back'), )

keyboard_discord_decorations_fantasy_avatar_2_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_fantasy_avatar_2_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_fantasy_avatar_2_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_fantasy_avatar_any_back'), )

keyboard_discord_decorations_fantasy_avatar_3_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_fantasy_avatar_3_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_fantasy_avatar_3_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_fantasy_avatar_any_back'), )

keyboard_discord_decorations_fantasy_avatar_4_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_fantasy_avatar_4_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_fantasy_avatar_4_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_fantasy_avatar_any_back'), )

keyboard_discord_decorations_fantasy_avatar_5_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_fantasy_avatar_5_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_fantasy_avatar_5_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_fantasy_avatar_any_back'), )

keyboard_discord_decorations_fantasy_avatar_6_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_fantasy_avatar_6_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_fantasy_avatar_6_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_fantasy_avatar_any_back'), )

keyboard_discord_decorations_fantasy_avatar_7_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_fantasy_avatar_7_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_fantasy_avatar_7_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_fantasy_avatar_any_back'), )

keyboard_discord_decorations_fantasy_avatar_8_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_fantasy_avatar_8_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_fantasy_avatar_8_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_fantasy_avatar_any_back'), )

keyboard_discord_decorations_anime = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_anime.add(
    InlineKeyboardButton(text='✨Украшения аватара', callback_data='discord_decorations_anime_avatar'),
    InlineKeyboardButton(text='✨Эффекты профиля', callback_data='discord_decorations_anime_profile'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_anytheme_back'),
)

keyboard_discord_decorations_anime_avatar = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_anime_avatar.add(
    InlineKeyboardButton(text='✨Излучая энергию', callback_data='discord_decorations_anime_avatar_1'),
    InlineKeyboardButton(text='✨Душа покидает тело', callback_data='discord_decorations_anime_avatar_2'),
    InlineKeyboardButton(text='✨Пот градом', callback_data='discord_decorations_anime_avatar_3'),
    InlineKeyboardButton(text='✨В мечтах', callback_data='discord_decorations_anime_avatar_4'),
    InlineKeyboardButton(text='✨Пришла любовь', callback_data='discord_decorations_anime_avatar_5'),
    InlineKeyboardButton(text='✨В шоке', callback_data='discord_decorations_anime_avatar_6'),
    InlineKeyboardButton(text='✨Гнев', callback_data='discord_decorations_anime_avatar_7'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_anime_anypiece_back'), )

keyboard_discord_decorations_anime_profile = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_anime_profile.add(
    InlineKeyboardButton(text='✨Волшебные сердца', callback_data='discord_decorations_anime_profile_1'),
    InlineKeyboardButton(text='✨Осколок', callback_data='discord_decorations_anime_profile_2'),
    InlineKeyboardButton(text='✨Бросок сюрикена', callback_data='discord_decorations_anime_profile_3'),
    InlineKeyboardButton(text='✨Пиковая мощность', callback_data='discord_decorations_anime_profile_4'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_anime_anypiece_back'), )

keyboard_discord_decorations_anime_profile_1_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_anime_profile_1_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_anime_profile_1_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_anime_profile_any_back'), )

keyboard_discord_decorations_anime_profile_2_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_anime_profile_2_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_anime_profile_2_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_anime_profile_any_back'), )

keyboard_discord_decorations_anime_profile_3_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_anime_profile_3_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_anime_profile_3_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_anime_profile_any_back'), )

keyboard_discord_decorations_anime_profile_4_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_anime_profile_4_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_anime_profile_4_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_anime_profile_any_back'), )

keyboard_discord_decorations_anime_avatar_1_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_anime_avatar_1_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_anime_avatar_1_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_anime_avatar_any_back'), )

keyboard_discord_decorations_anime_avatar_2_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_anime_avatar_2_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_anime_avatar_2_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_anime_avatar_any_back'), )

keyboard_discord_decorations_anime_avatar_3_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_anime_avatar_3_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_anime_avatar_3_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_anime_avatar_any_back'), )

keyboard_discord_decorations_anime_avatar_4_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_anime_avatar_4_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_anime_avatar_4_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_anime_avatar_any_back'), )

keyboard_discord_decorations_anime_avatar_5_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_anime_avatar_5_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_anime_avatar_5_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_anime_avatar_any_back'), )

keyboard_discord_decorations_anime_avatar_6_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_anime_avatar_6_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_anime_avatar_6_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_anime_avatar_any_back'), )

keyboard_discord_decorations_anime_avatar_7_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_anime_avatar_7_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_anime_avatar_7_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_anime_avatar_any_back'), )

keyboard_discord_decorations_breakfast = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_breakfast.add(
    InlineKeyboardButton(text='🥐Украшения аватара', callback_data='discord_decorations_breakfast_avatar'),
    InlineKeyboardButton(text='🥐Эффекты профиля', callback_data='discord_decorations_breakfast_profile'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_anytheme_back'),
)

keyboard_discord_decorations_breakfast_avatar = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_breakfast_avatar.add(
    InlineKeyboardButton(text='🥐Тост', callback_data='discord_decorations_breakfast_avatar_1'),
    InlineKeyboardButton(text='🥐Утренний кофе', callback_data='discord_decorations_breakfast_avatar_2'),
    InlineKeyboardButton(text='🥐Жаренное яйцо', callback_data='discord_decorations_breakfast_avatar_3'),
    InlineKeyboardButton(text='🥐Черничный джем', callback_data='discord_decorations_breakfast_avatar_4'),
    InlineKeyboardButton(text='🥐Пончик', callback_data='discord_decorations_breakfast_avatar_5'),
    InlineKeyboardButton(text='🥐Оладушки', callback_data='discord_decorations_breakfast_avatar_6'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_breakfast_anypiece_back'), )

keyboard_discord_decorations_breakfast_profile = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_breakfast_profile.add(
    InlineKeyboardButton(text='🥐Discord-Os', callback_data='discord_decorations_breakfast_profile_1'),
    InlineKeyboardButton(text='🥐Сытный завтрак', callback_data='discord_decorations_breakfast_profile_2'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_breakfast_anypiece_back'), )

keyboard_discord_decorations_breakfast_profile_1_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_breakfast_profile_1_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_breakfast_profile_1_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_breakfast_profile_any_back'), )

keyboard_discord_decorations_breakfast_profile_2_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_breakfast_profile_2_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_breakfast_profile_2_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_breakfast_profile_any_back'), )

keyboard_discord_decorations_breakfast_avatar_1_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_breakfast_avatar_1_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_breakfast_avatar_1_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_breakfast_avatar_any_back'), )

keyboard_discord_decorations_breakfast_avatar_2_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_breakfast_avatar_2_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_breakfast_avatar_2_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_breakfast_avatar_any_back'), )

keyboard_discord_decorations_breakfast_avatar_3_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_breakfast_avatar_3_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_breakfast_avatar_3_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_breakfast_avatar_any_back'), )

keyboard_discord_decorations_breakfast_avatar_4_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_breakfast_avatar_4_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_breakfast_avatar_4_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_breakfast_avatar_any_back'), )

keyboard_discord_decorations_breakfast_avatar_5_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_breakfast_avatar_5_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_breakfast_avatar_5_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_breakfast_avatar_any_back'), )

keyboard_discord_decorations_breakfast_avatar_6_buy = InlineKeyboardMarkup(row_width=1)
keyboard_discord_decorations_breakfast_avatar_6_buy.add(
    InlineKeyboardButton(text='Купить', callback_data='discord_decorations_breakfast_avatar_6_buy'),
    InlineKeyboardButton(text='Назад', callback_data='discord_decorations_breakfast_avatar_any_back'), )


def buy_menu(isurl=True, url='', bill=''):
    yomoney_menu = InlineKeyboardMarkup(row_width=1)
    if isurl:
        webapp = WebAppInfo(url=url)
        yomoney_menu.add(InlineKeyboardButton(text='Оплатить', web_app=webapp))
    yomoney_menu.add(InlineKeyboardButton(text='Проверить оплату', callback_data=f'check__{bill}'))
    yomoney_menu.add(InlineKeyboardButton(text='Отмена', callback_data=f'cancel_insert'))
    return yomoney_menu


def review_kb(order_id):
    keyboard_review = InlineKeyboardMarkup(row_width=1)
    keyboard_review.add(InlineKeyboardButton(text='Оставить отзыв', callback_data=f'addreview_{order_id}'))
    return keyboard_review


choose_insert = InlineKeyboardMarkup(row_width=1)
choose_insert.add(InlineKeyboardButton(text='Отмена', callback_data='choose_insert_cancel'))

keyboard_discord = InlineKeyboardMarkup(row_width=1)
keyboard_discord.add(InlineKeyboardButton(text='Nitro', callback_data='discord_nitro'),
                     InlineKeyboardButton(text='Украшения', callback_data='discord_decorations'),
                     InlineKeyboardButton(text='Назад ко всем категориям', callback_data='discord_back'), )

keyboard_nitro = InlineKeyboardMarkup(row_width=1)
keyboard_nitro.add(InlineKeyboardButton(text=f'Nitro Full(1 месяц) QR',
                                        callback_data='ntr_1m_qr'),
                   InlineKeyboardButton(text=f'Nitro Full(1 год) QR', callback_data='ntr_1y_qr'),
                   InlineKeyboardButton(text=f'Nitro Full(1 месяц) без входа',
                                        callback_data='ntr_1m_no_log'),
                   InlineKeyboardButton(text=f'Nitro Full(1 год) без входа',
                                        callback_data='ntr_1y_no_log'),
                   InlineKeyboardButton(text=f'Назад', callback_data='ntr_back'), )

keyboard_buy_nitro_1m_qr = InlineKeyboardMarkup(row_width=1)
keyboard_buy_nitro_1m_qr.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_nitro_1m_qr'),
                             InlineKeyboardButton(text='Назад', callback_data='buy_back'))

keyboard_buy_nitro_1y_qr = InlineKeyboardMarkup(row_width=1)
keyboard_buy_nitro_1y_qr.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_nitro_1y_qr'),
                             InlineKeyboardButton(text='Назад', callback_data='buy_back'))

keyboard_buy_nitro_1m = InlineKeyboardMarkup(row_width=1)
keyboard_buy_nitro_1m.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_nitro_1m'),
                          InlineKeyboardButton(text='Назад', callback_data='buy_back'))

keyboard_buy_nitro_1y = InlineKeyboardMarkup(row_width=1)
keyboard_buy_nitro_1y.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_nitro_1y'),
                          InlineKeyboardButton(text='Назад', callback_data='buy_back'))

keyboard_buy_nitro_1m_noreg = InlineKeyboardMarkup(row_width=1)
keyboard_buy_nitro_1m_noreg.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_nitro_1m_noreg'),
                                InlineKeyboardButton(text='Назад', callback_data='buy_back'))

keyboard_buy_nitro_1y_noreg = InlineKeyboardMarkup(row_width=1)
keyboard_buy_nitro_1y_noreg.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_nitro_1y_noreg'),
                                InlineKeyboardButton(text='Назад', callback_data='buy_back'))

keyboard_genshin = InlineKeyboardMarkup(row_width=1)
keyboard_genshin.add(InlineKeyboardButton(text=f'Благословение полой луны', callback_data='gnsh_moon'),
                     InlineKeyboardButton(text=f'60 Кристаллов Сотворения', callback_data='gnsh_60k'),
                     InlineKeyboardButton(text=f'300+30 Кристаллов Сотворения',
                                          callback_data='gnsh_300k'),
                     InlineKeyboardButton(text=f'980+110 Кристаллов Сотворения',
                                          callback_data='gnsh_980k'),
                     InlineKeyboardButton(text=f'1980+260 Кристаллов Сотворения',
                                          callback_data='gnsh_1980k'),
                     InlineKeyboardButton(text=f'3280+600 Кристаллов Сотворения',
                                          callback_data='gnsh_3280k'),
                     InlineKeyboardButton(text=f'6480+1600 Кристаллов Сотворения',
                                          callback_data='gnsh_6480k'),
                     InlineKeyboardButton(text=f'Назад ко всем категориям', callback_data='gnsh_back'),
                     )

keyboard_genshin_moon = InlineKeyboardMarkup(row_width=1)
keyboard_genshin_moon.add(InlineKeyboardButton(text='Купить', callback_data='buy_gnsh_moon'),
                          InlineKeyboardButton(text='Назад', callback_data='buy_gnsh_back'))

keyboard_genshin_60k = InlineKeyboardMarkup(row_width=1)
keyboard_genshin_60k.add(InlineKeyboardButton(text='Купить', callback_data='buy_gnsh_60k'),
                         InlineKeyboardButton(text='Назад', callback_data='buy_gnsh_back'))

keyboard_genshin_300k = InlineKeyboardMarkup(row_width=1)
keyboard_genshin_300k.add(InlineKeyboardButton(text='Купить', callback_data='buy_gnsh_300k'),
                          InlineKeyboardButton(text='Назад', callback_data='buy_gnsh_back'))

keyboard_genshin_980k = InlineKeyboardMarkup(row_width=1)
keyboard_genshin_980k.add(InlineKeyboardButton(text='Купить', callback_data='buy_gnsh_980k'),
                          InlineKeyboardButton(text='Назад', callback_data='buy_gnsh_back'))

keyboard_genshin_1980k = InlineKeyboardMarkup(row_width=1)
keyboard_genshin_1980k.add(InlineKeyboardButton(text='Купить', callback_data='buy_gnsh_1980k'),
                           InlineKeyboardButton(text='Назад', callback_data='buy_gnsh_back'))

keyboard_genshin_3280k = InlineKeyboardMarkup(row_width=1)
keyboard_genshin_3280k.add(InlineKeyboardButton(text='Купить', callback_data='buy_gnsh_3280k'),
                           InlineKeyboardButton(text='Назад', callback_data='buy_gnsh_back'))

keyboard_genshin_6480k = InlineKeyboardMarkup(row_width=1)
keyboard_genshin_6480k.add(InlineKeyboardButton(text='Купить', callback_data='buy_gnsh_6480k'),
                           InlineKeyboardButton(text='Назад', callback_data='buy_gnsh_back'))

keyboard_honkai = InlineKeyboardMarkup(row_width=1)
keyboard_honkai.add(
    InlineKeyboardButton(text=f'Пропуск снабжения экспресса', callback_data='hon_sp'),
    InlineKeyboardButton(text=f'60 Сущность дневних снов', callback_data='hon_60k'),
    InlineKeyboardButton(text=f'300+30 Сущность дневних снов',
                         callback_data='hon_300k'),
    InlineKeyboardButton(text=f'980+110 Сущность дневних снов',
                         callback_data='hon_980k'),
    InlineKeyboardButton(text=f'1980+260 Сущность дневних снов',
                         callback_data='hon_1980k'),
    InlineKeyboardButton(text=f'3280+600 Сущность дневних снов',
                         callback_data='hon_3280k'),
    InlineKeyboardButton(text=f'6480+1600 Сущность дневних снов',
                         callback_data='hon_6480k'),
    InlineKeyboardButton(text=f'Назад ко всем категориям', callback_data='hon_back'),
)

keyboard_hon_sp = InlineKeyboardMarkup(row_width=1)
keyboard_hon_sp.add(InlineKeyboardButton(text='Купить', callback_data='buy_hon_sp'),
                    InlineKeyboardButton(text='Назад', callback_data='buy_hon_back'))

keyboard_hon_60k = InlineKeyboardMarkup(row_width=1)
keyboard_hon_60k.add(InlineKeyboardButton(text='Купить', callback_data='buy_hon_60k'),
                     InlineKeyboardButton(text='Назад', callback_data='buy_hon_back'))

keyboard_hon_300k = InlineKeyboardMarkup(row_width=1)
keyboard_hon_300k.add(InlineKeyboardButton(text='Купить', callback_data='buy_hon_300k'),
                      InlineKeyboardButton(text='Назад', callback_data='buy_hon_back'))

keyboard_hon_980k = InlineKeyboardMarkup(row_width=1)
keyboard_hon_980k.add(InlineKeyboardButton(text='Купить', callback_data='buy_hon_980k'),
                      InlineKeyboardButton(text='Назад', callback_data='buy_hon_back'))

keyboard_hon_1980k = InlineKeyboardMarkup(row_width=1)
keyboard_hon_1980k.add(InlineKeyboardButton(text='Купить', callback_data='buy_hon_1980k'),
                       InlineKeyboardButton(text='Назад', callback_data='buy_hon_back'))

keyboard_hon_3280k = InlineKeyboardMarkup(row_width=1)
keyboard_hon_3280k.add(InlineKeyboardButton(text='Купить', callback_data='buy_hon_3280k'),
                       InlineKeyboardButton(text='Назад', callback_data='buy_hon_back'))

keyboard_hon_6480k = InlineKeyboardMarkup(row_width=1)
keyboard_hon_6480k.add(InlineKeyboardButton(text='Купить', callback_data='buy_hon_6480k'),
                       InlineKeyboardButton(text='Назад', callback_data='buy_hon_back'))

keyboard_tg = InlineKeyboardMarkup(row_width=1)
keyboard_tg.add(InlineKeyboardButton(text=f'Telegram Premium QR(1 месяц)',
                                     callback_data='tg_1m_qr'),
                InlineKeyboardButton(text=f'Telegram Premium QR(1 год)',
                                     callback_data='tg_1y_qr'),
                InlineKeyboardButton(text=f'Telegram Premium без входа(1 месяц)',
                                     callback_data='tg_1m_noreg'),
                InlineKeyboardButton(text=f'Telegram Premium без входа(1 год)',
                                     callback_data='tg_1y_noreg'),

                InlineKeyboardButton(text=f'Назад ко всем категориям', callback_data='tg_back'), )

keyboard_buy_tg_1m_qr = InlineKeyboardMarkup(row_width=1)
keyboard_buy_tg_1m_qr.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_tg_1m_qr'),
                          InlineKeyboardButton(text='Назад', callback_data='buy_tg_back'))

keyboard_buy_tg_1y_qr = InlineKeyboardMarkup(row_width=1)
keyboard_buy_tg_1y_qr.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_tg_1y_qr'),
                          InlineKeyboardButton(text='Назад', callback_data='buy_tg_back'))

keyboard_buy_tg_1m_noreg = InlineKeyboardMarkup(row_width=1)
keyboard_buy_tg_1m_noreg.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_tg_1m_noreg'),
                             InlineKeyboardButton(text='Назад', callback_data='buy_tg_back'))

keyboard_buy_tg_1y_noreg = InlineKeyboardMarkup(row_width=1)
keyboard_buy_tg_1y_noreg.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_tg_1y_noreg'),
                             InlineKeyboardButton(text='Назад', callback_data='buy_tg_back'))

keyboard_spotify = InlineKeyboardMarkup(row_width=1)
keyboard_spotify.add(InlineKeyboardButton(text='Spotify Premium(1 месяц)', callback_data='spotify_1m'),
                     InlineKeyboardButton(text='Spotify Premium(3 месяца)', callback_data='spotify_3m'),
                     InlineKeyboardButton(text='Spotify Premium(6 месяцев)', callback_data='spotify_6m'),
                     InlineKeyboardButton(text='Spotify Premium(12 месяцев)', callback_data='spotify_12m'),
                     InlineKeyboardButton(text='Назад ко всем категориям', callback_data='spotify_back'), )

keyboard_buy_spotify_1m = InlineKeyboardMarkup(row_width=1)
keyboard_buy_spotify_1m.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_spotify_1m'),
                            InlineKeyboardButton(text='Назад', callback_data='buy_spotify_back'))

keyboard_buy_spotify_3m = InlineKeyboardMarkup(row_width=1)
keyboard_buy_spotify_3m.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_spotify_3m'),
                            InlineKeyboardButton(text='Назад', callback_data='buy_spotify_back'))

keyboard_buy_spotify_6m = InlineKeyboardMarkup(row_width=1)
keyboard_buy_spotify_6m.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_spotify_6m'),
                            InlineKeyboardButton(text='Назад', callback_data='buy_spotify_back'))

keyboard_buy_spotify_12m = InlineKeyboardMarkup(row_width=1)
keyboard_buy_spotify_12m.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_spotify_12m'),
                             InlineKeyboardButton(text='Назад', callback_data='buy_spotify_back'))

keyboard_fortnite = InlineKeyboardMarkup(row_width=1)
keyboard_fortnite.add(InlineKeyboardButton(text='1000 В-баксов', callback_data='fortnite_1000'),
                      InlineKeyboardButton(text='2800 В-баксов', callback_data='fortnite_2800'),
                      InlineKeyboardButton(text='5000 В-баксов', callback_data='fortnite_5000'),
                      InlineKeyboardButton(text='13500 В-баксов', callback_data='fortnite_13500'),
                      InlineKeyboardButton(text='Назад ко всем категориям', callback_data='fortnite_back'),
                      )

keyboard_buy_fortnite_1000 = InlineKeyboardMarkup(row_width=1)
keyboard_buy_fortnite_1000.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_fortnite_1000'),
                               InlineKeyboardButton(text='Назад', callback_data='buy_fortnite_back'))

keyboard_buy_fortnite_2800 = InlineKeyboardMarkup(row_width=1)
keyboard_buy_fortnite_2800.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_fortnite_2800'),
                               InlineKeyboardButton(text='Назад', callback_data='buy_fortnite_back'))

keyboard_buy_fortnite_5000 = InlineKeyboardMarkup(row_width=1)
keyboard_buy_fortnite_5000.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_fortnite_5000'),
                               InlineKeyboardButton(text='Назад', callback_data='buy_fortnite_back'))

keyboard_buy_fortnite_13500 = InlineKeyboardMarkup(row_width=1)
keyboard_buy_fortnite_13500.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_fortnite_13500'),
                                InlineKeyboardButton(text='Назад', callback_data='buy_fortnite_back'))

keyboard_buy_xbox = InlineKeyboardMarkup(row_width=1)
keyboard_buy_xbox.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_xbox'),
                      InlineKeyboardButton(text='Назад', callback_data='buy_xbox_back'))

keyboard_buy_ya = InlineKeyboardMarkup(row_width=1)
keyboard_buy_ya.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_ya'),
                    InlineKeyboardButton(text='Назад', callback_data='buy_ya_back'))

keyboard_main = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_main.add('Товары', 'Профиль').add('Руководство', 'Помощь')

keyboard_main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_main_admin.add('Товары', 'Профиль').add('Руководство', 'Помощь').add('Админ-панель')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Рассылка (/sendall *text*)').add('+бл (/addmn *id* *amm*)').add('измц (/cgprice *name* *price*)').add(
    'польз (/useractive)').add('забл (/block *id*)').add('разбл (/unblock *id*)').add('забл_спис /list_blocked').add(
    'отп_чек (/send_check#*id*#*item*#*price*')

keyboard_profile = InlineKeyboardMarkup(row_width=2)
keyboard_profile.add(InlineKeyboardButton(text='Пополнить', callback_data='profile_insert'),
                     InlineKeyboardButton(text='Покупки', callback_data='profile_history'), )

keyboard_top_up = InlineKeyboardMarkup(row_width=1)
keyboard_top_up.add(InlineKeyboardButton(text='Пополнить', callback_data='profile_insert'))

keyboard_stock_inl = InlineKeyboardMarkup(row_width=2)
keyboard_stock_inl.add(InlineKeyboardButton(text='💜Discord', callback_data='btndiscord'),
                       InlineKeyboardButton(text='🟣Яндекс Плюс', callback_data='btnyandex'),
                       InlineKeyboardButton(text='🔷Telegram Premium', callback_data='btntg'),
                       InlineKeyboardButton(text='🟢Spotify Premium', callback_data='btnspotify'),
                       InlineKeyboardButton(text='🎮Xbox Game Pass', callback_data='btnxbox'),
                       InlineKeyboardButton(text='✨Fortnite', callback_data='btnfortnite'),
                       InlineKeyboardButton(text='💎Genshin Impact', callback_data='btngenshin'),
                       InlineKeyboardButton(text='💎Honkai: Star Rail', callback_data='btnhonkai'),
                       InlineKeyboardButton(text='🌐Другие сервисы', callback_data='btnotherserv'),
                       ),
keyboard_other_back = InlineKeyboardMarkup(row_width=1)
keyboard_other_back.add(InlineKeyboardButton(text='Назад ко всем категориям', callback_data='buy_other_back'))

keyboard_review_text_empty = InlineKeyboardMarkup(row_width=1)
keyboard_review_text_empty.add(InlineKeyboardButton(text='Без текста, только оценка', callback_data='review_notext'))

keyboard_review_mark = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
keyboard_review_mark.add('❤️').add('👎').add('Не оставлять отзыв')

cancel = ReplyKeyboardMarkup(resize_keyboard=True)
cancel.add('Отмена')
