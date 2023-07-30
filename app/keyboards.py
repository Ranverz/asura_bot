from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup

from app.var import price_nitro_1m, price_nitro_1y, price_nitro_1m_qr, price_nitro_1y_qr, \
    price_nitro_1m_noreg, price_nitro_1y_noreg, price_60k, price_300k, price_980k, price_1980k, price_3280k, \
    price_6480k, price_moon, price_sp, price_hon_60k, price_hon_300k, price_hon_980k, price_hon_1980k, price_hon_3280k, \
    price_hon_6480k


def buy_menu(isurl=True, url='', bill=''):
    yomoney_menu = InlineKeyboardMarkup(row_width=1)
    if isurl:
        yomoney_menu.add(InlineKeyboardButton(text='Оплатить', url=url))
    yomoney_menu.add(InlineKeyboardButton(text='Проверить оплату', callback_data=f'check__{bill}'))
    yomoney_menu.add(InlineKeyboardButton(text='Отмена', callback_data=f'cancel_insert'))
    return yomoney_menu


choose_insert = InlineKeyboardMarkup(row_width=1)
choose_insert.add(InlineKeyboardButton(text='Отмена', callback_data='choose_insert_cancel'))

keyboard_cheat = InlineKeyboardMarkup(row_width=1)
keyboard_cheat.add(InlineKeyboardButton(text='Подписка на 7 дней', callback_data='cheat_7d'),
                   InlineKeyboardButton(text='Подписка на 30 дней', callback_data='cheat_30d'),
                   InlineKeyboardButton(text='Подписка на 180 дней', callback_data='cheat_180d'),
                   InlineKeyboardButton(text='Подписка на 1 год', callback_data='cheat_1y'),
                   InlineKeyboardButton(text='Назад ко всем категориям', callback_data='cheat_back'), )

keyboard_nitro = InlineKeyboardMarkup(row_width=1)
keyboard_nitro.add(InlineKeyboardButton(text=f'Nitro Full(1 месяц) QR | {price_nitro_1m_qr}₽',
                                        callback_data='ntr_1m_qr'),
                   InlineKeyboardButton(text=f'Nitro Full(1 год) QR | {price_nitro_1y_qr}₽', callback_data='ntr_1y_qr'),
                   InlineKeyboardButton(text=f'Nitro Full(1 месяц) без входа | {price_nitro_1m_noreg}₽',
                                        callback_data='ntr_1m_no_log'),
                   InlineKeyboardButton(text=f'Nitro Full(1 год) без входа | {price_nitro_1y_noreg}₽',
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
keyboard_genshin.add(InlineKeyboardButton(text=f'Благословение полой луны | {price_moon}₽', callback_data='gnsh_moon'),
                     InlineKeyboardButton(text=f'60 Кристаллов Сотворения | {price_60k}₽', callback_data='gnsh_60k'),
                     InlineKeyboardButton(text=f'300+30 Кристаллов Сотворения | {price_300k}₽',
                                          callback_data='gnsh_300k'),
                     InlineKeyboardButton(text=f'980+110 Кристаллов Сотворения | {price_980k}₽',
                                          callback_data='gnsh_980k'),
                     InlineKeyboardButton(text=f'1980+260 Кристаллов Сотворения | {price_1980k}₽',
                                          callback_data='gnsh_1980k'),
                     InlineKeyboardButton(text=f'3280+600 Кристаллов Сотворения | {price_3280k}₽',
                                          callback_data='gnsh_3280k'),
                     InlineKeyboardButton(text=f'6480+1600 Кристаллов Сотворения | {price_6480k}₽',
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
    InlineKeyboardButton(text=f'Пропуск снабжения экспресса | {price_sp}₽', callback_data='hon_sp'),
    InlineKeyboardButton(text=f'60 Сущность дневних снов | {price_hon_60k}₽', callback_data='hon_60k'),
    InlineKeyboardButton(text=f'300+30 Сущность дневних снов | {price_hon_300k}₽',
                         callback_data='hon_300k'),
    InlineKeyboardButton(text=f'980+110 Сущность дневних снов | {price_hon_980k}₽',
                         callback_data='hon_980k'),
    InlineKeyboardButton(text=f'1980+260 Сущность дневних снов | {price_hon_1980k}₽',
                         callback_data='hon_1980k'),
    InlineKeyboardButton(text=f'3280+600 Сущность дневних снов | {price_hon_3280k}₽',
                         callback_data='hon_3280k'),
    InlineKeyboardButton(text=f'6480+1600 Сущность дневних снов | {price_hon_6480k}₽',
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

# InlineKeyboardButton(text=f'Nitro Full(1 месяц) | {price_nitro_1m}₽', callback_data='ntr_1m'),
# InlineKeyboardButton(text=f'Nitro Full(1 год) | {price_nitro_1y}₽', callback_data='ntr_1y'),

keyboard_main = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_main.add('Товары', 'Профиль').add('Руководство', 'Помощь')

keyboard_main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_main_admin.add('Товары', 'Профиль').add('Руководство', 'Помощь').add('Админ-панель')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Рассылка(/sendall)').add('+бл(/addmn id amm)')

keyboard_profile = InlineKeyboardMarkup(row_width=2)
keyboard_profile.add(InlineKeyboardButton(text='Пополнить', callback_data='profile_insert'),
                     InlineKeyboardButton(text='Покупки', callback_data='profile_history'), )

keyboard_stock_inl = InlineKeyboardMarkup(row_width=1)
keyboard_stock_inl.add(InlineKeyboardButton(text='Discord Nitro', callback_data='btndiscord'),
                       InlineKeyboardButton(text='Genshin Impact', callback_data='btngenshin'),
                       InlineKeyboardButton(text='Honkai: Star Rail', callback_data='btnhonkai')),
# InlineKeyboardButton(text='Csgo cheat', callback_data='cheat'),

cancel = ReplyKeyboardMarkup(resize_keyboard=True)
cancel.add('Отмена')
