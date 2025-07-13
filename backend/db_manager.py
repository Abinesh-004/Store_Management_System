import sqlite3

def get_connection():
    return sqlite3.connect("database.db")

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT CHECK(role IN ('salesperson', 'admin', 'superuser')),
            is_approved INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()
