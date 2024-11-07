import sqlite3
import json
from models.user_session import UserSession

def init_db(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_sessions (user_id TEXT PRIMARY KEY, language TEXT, message_history TEXT)''')
    conn.commit()
    return conn

def save_session(conn, session):
    cursor = conn.cursor()
    cursor.execute('''INSERT OR REPLACE INTO user_sessions (user_id, language, message_history) VALUES (?, ?, ?)''', (session.user_id, session.language, json.dumps(session.message_history)))
    conn.commit()

def load_session(conn, user_id):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user_sessions WHERE user_id = ?', (user_id,))
    row = cursor.fetchone()
    if row:
        session = UserSession(row[0], row[1])
        session.message_history = json.loads(row[2])
        return session
    return None
