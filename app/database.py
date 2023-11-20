import sqlite3 as sq
import datetime
from app.var import moscow_tz
from dotenv import load_dotenv
import os

load_dotenv()
conn = sq.connect(os.getenv('DB_NAME'))
cursor = conn.cursor()


async def db_start():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER,
            registration_date TEXT,
            balance REAL,
            bought_items INTEGER,
            active INTEGER DEFAULT 1,
            blocked INTEGER DEFAULT 0
        )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS history(
                purch_id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER,
                name TEXT,
                price REAL,
                purc_time TEXT
            )
        ''')

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS items(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    price REAL,
                    UNIQUE(name)
                )
            ''')

    items_data = [
        ('ds_ntr_1m_qr', 299),
        ('ds_ntr_1y_qr', 2939),
        ('ds_ntr_1m_noreg', 349),
        ('ds_ntr_1y_noreg', 2989),

        ('ds_dec_limited_avatar', 279),
        ('ds_dec_limited_profile', 349),

        ('ds_dec_fantasy_avatar', 349),
        ('ds_dec_fantasy_profile', 369),
        ('ds_dec_anime_avatar', 279),
        ('ds_dec_anime_profile', 369),
        ('ds_dec_breakfast_avatar', 139),
        ('ds_dec_breakfast_profile', 369),

        ('gnsh_moon', 429),
        ('gnsh_60k', 89),
        ('gnsh_300k', 429),
        ('gnsh_980k', 1299),
        ('gnsh_1980k', 2769),
        ('gnsh_3280k', 4269),
        ('gnsh_6480k', 8390),

        ('hon_sp', 429),
        ('hon_60k', 89),
        ('hon_300k', 428),
        ('hon_980k', 1299),
        ('hon_1980k', 2769),
        ('hon_3280k', 4269),
        ('hon_6480k', 8579),

        ('tg_1m_qr', 239),
        ('tg_1y_qr', 1760),
        ('tg_1m_noreg', 289),
        ('tg_1y_noreg', 1810),

        ('ya', 150),

        ('xbox', 819),

        ('spotify_1m', 159),
        ('spotify_3m', 469),
        ('spotify_6m', 939),
        ('spotify_12m', 1599),

        ('fortnite_1000', 469),
        ('fortnite_2800', 1179),
        ('fortnite_5000', 1959),
        ('fortnite_13500', 4699),

    ]

    cursor.executemany('''INSERT OR REPLACE INTO `items` (name, price) VALUES (?, ?)''', items_data)

    conn.commit()


async def cmd_start_db(user_id):
    user = cursor.execute(f'''SELECT * FROM users WHERE telegram_id = ?''', (user_id,)).fetchone()
    if not user:
        cursor.execute(
            f'''INSERT INTO users (telegram_id, registration_date, balance, bought_items) VALUES (?, ?, ?, ?)''',
            (user_id, str(datetime.datetime.now(moscow_tz)).split('.')[0], 0.0, 0,))
        last_id = cursor.lastrowid
        conn.commit()
        return last_id


async def user_exists(user_id):
    user = cursor.execute(f'''SELECT * FROM users WHERE telegram_id = ?''', (user_id,)).fetchone()
    if user:
        return True
    else:
        return False


async def set_block_user_status(user_id, val):
    cursor.execute(f'''UPDATE users SET blocked = ? WHERE telegram_id = ?''', (val, user_id,))
    conn.commit()


async def show_blocked_users():
    users = cursor.execute(f'''SELECT telegram_id FROM users WHERE blocked = 1''').fetchall()
    return users


async def user_is_active(user_id):
    user = cursor.execute(f'''SELECT active FROM users WHERE telegram_id = ?''', (user_id,)).fetchone()
    if user[0] == 1:
        return True
    else:
        return False


async def show_profile(user_id):
    user = cursor.execute(f'''SELECT * FROM users WHERE telegram_id = ?''', (user_id,)).fetchone()
    return user


async def show_history(user_id):
    user = cursor.execute(f'''SELECT * FROM history WHERE telegram_id = ?''', (user_id,)).fetchall()
    return user


async def show_money(user_id):
    user = cursor.execute(f'''SELECT balance FROM users WHERE telegram_id = ?''', (user_id,)).fetchone()
    return user[0]


async def add_money(user_id, money):
    cursor.execute("UPDATE users SET balance = balance + ? WHERE telegram_id = ?",
                   (money, user_id,))
    conn.commit()


async def add_purchase(user_id, item_name, price, tm):
    cursor.execute("UPDATE `users` SET `bought_items` = bought_items + 1 WHERE `telegram_id` = ?",
                   (user_id,))
    cursor.execute(
        '''INSERT INTO `history` (telegram_id, name, price, purc_time) VALUES (?, ?, ?, ?)''',
        (user_id, item_name, price, tm,))
    conn.commit()


async def show_price(item_name):
    pr = cursor.execute('''SELECT price FROM items WHERE name = ?''', (item_name,)).fetchone()
    return int(pr[0])


async def change_price(item_name, price):
    cursor.execute('''UPDATE items SET price = ? WHERE name = ?''', (price, item_name,))
    conn.commit()


async def show_purchase_id(user_id, tm):
    user = cursor.execute('''SELECT purch_id FROM history WHERE telegram_id = ? and purc_time = ?''',
                          (user_id, tm)).fetchone()
    return user[0]


async def show_purchase_info(user_id, purc_id):
    user = cursor.execute(
        '''SELECT purc_time, name FROM history WHERE telegram_id = ? and purch_id = ?''',
        (user_id, purc_id,)).fetchone()
    return user


async def show_active_users():
    user = cursor.execute(
        '''SELECT telegram_id FROM users WHERE active = 1''').fetchall()
    return user


async def show_unactive_users():
    user = cursor.execute(
        '''SELECT telegram_id FROM users WHERE active = 0''').fetchall()
    return user


async def set_active(user_id, active):
    cursor.execute('''UPDATE users SET active = ? WHERE telegram_id = ?''', (active, user_id,))
    conn.commit()


async def get_users():
    user = cursor.execute("SELECT telegram_id, active FROM users").fetchall()
    return user
