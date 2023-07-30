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
            active INTEGER DEFAULT 1
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
                    price REAL
                )
            ''')

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


async def show_purchase_id(user_id, tm):
    user = cursor.execute('''SELECT purch_id FROM history WHERE telegram_id = ? and purc_time = ?''',
                          (user_id, tm)).fetchone()
    return user[0]


async def show_last_purchase_id(user_id):
    user = cursor.execute(
        '''SELECT purch_id, purc_time FROM history WHERE telegram_id = ? ORDER BY purch_id DESC LIMIT 1''',
        (user_id,)).fetchone()
    return user


async def set_active(user_id, active):
    cursor.execute('''UPDATE users SET active = ? WHERE telegram_id = ?''', (active, user_id,))
    conn.commit()


async def get_users():
    user = cursor.execute("SELECT telegram_id, active FROM users").fetchall()
    return user
