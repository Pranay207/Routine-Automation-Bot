import sqlite3
from datetime import datetime

DB_PATH = "app/database.db"

# Initialize DB
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT,
            status TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Log task completion
def log_task(task_name, status):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO tasks (task_name, status, timestamp) VALUES (?, ?, ?)",
              (task_name, status, timestamp))
    conn.commit()
    conn.close()

# Get all logs
def get_logs():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM tasks ORDER BY timestamp DESC")
    rows = c.fetchall()
    conn.close()
    return rows

