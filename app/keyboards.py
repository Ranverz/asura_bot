from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup


def buy_menu(isurl=True, url='', bill=''):
    yomoney_menu = InlineKeyboardMarkup(row_width=1)
    if isurl:
        yomoney_menu.add(InlineKeyboardButton(text='Оплатить', url=url))
    yomoney_menu.add(InlineKeyboardButton(text='Проверить оплату', callback_data=f'check__{bill}'))
    yomoney_menu.add(InlineKeyboardButton(text='Отмена', callback_data=f'cancel_insert'))
    return yomoney_menu


choose_insert = InlineKeyboardMarkup(row_width=1)
choose_insert.add(InlineKeyboardButton(text='Отмена', callback_data='choose_insert_cancel'))

keyboard_nitro = InlineKeyboardMarkup(row_width=1)
keyboard_nitro.add(InlineKeyboardButton(text=f'Nitro Full(1 месяц) QR',
                                        callback_data='ntr_1m_qr'),
                   InlineKeyboardButton(text=f'Nitro Full(1 год) QR', callback_data='ntr_1y_qr'),
                   InlineKeyboardButton(text=f'Nitro Full(1 месяц) без входа',
                                        callback_data='ntr_1m_no_log'),
                   InlineKeyboardButton(text=f'Nitro Full(1 год) без входа',
                                        callback_data='ntr_1y_no_log'),
                   InlineKeyboardButton(text=f'Назад ко всем категориям', callback_data='ntr_back'), )

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

                InlineKeyboardButton(text=f'Назад ко всем категориям', callback_data='tg_back'), )

keyboard_buy_tg_1m = InlineKeyboardMarkup(row_width=1)
keyboard_buy_tg_1m.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_tg_1m'),
                       InlineKeyboardButton(text='Назад', callback_data='buy_tg_back'))

keyboard_buy_tg_1y = InlineKeyboardMarkup(row_width=1)
keyboard_buy_tg_1y.add(InlineKeyboardButton(text='Купить', callback_data='buy_buy_tg_1y'),
                       InlineKeyboardButton(text='Назад', callback_data='buy_tg_back'))

keyboard_main = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_main.add('Товары', 'Профиль').add('Руководство', 'Помощь')

keyboard_main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_main_admin.add('Товары', 'Профиль').add('Руководство', 'Помощь').add('Админ-панель')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Рассылка (/sendall *text*)').add('+бл (/addmn *id* *amm*)').add('измц (/cgprice *name* *price*)').add(
    'польз (/useractive)').add('забл (/block *id*)').add('разбл (/unblock *id*)').add('забл_спис /list_blocked')

keyboard_profile = InlineKeyboardMarkup(row_width=2)
keyboard_profile.add(InlineKeyboardButton(text='Пополнить', callback_data='profile_insert'),
                     InlineKeyboardButton(text='Покупки', callback_data='profile_history'), )

keyboard_stock_inl = InlineKeyboardMarkup(row_width=1)
keyboard_stock_inl.add(InlineKeyboardButton(text='Discord Nitro', callback_data='btndiscord'),
                       InlineKeyboardButton(text='Telegram Premium', callback_data='btntg'),
                       InlineKeyboardButton(text='Genshin Impact', callback_data='btngenshin'),
                       InlineKeyboardButton(text='Honkai: Star Rail', callback_data='btnhonkai'),
                       ),
# InlineKeyboardButton(text='Csgo cheat', callback_data='cheat'),

cancel = ReplyKeyboardMarkup(resize_keyboard=True)
cancel.add('Отмена')
