import sqlite3

def connect():
    return sqlite3.connect("logs.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            log TEXT,
            threat TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Table created successfully")

def insert_log(log, threat):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO logs (log, threat) VALUES (?, ?)", (log, threat))

    conn.commit()
    conn.close()

def fetch_logs():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logs")
    data = cursor.fetchall()

    conn.close()
    return data