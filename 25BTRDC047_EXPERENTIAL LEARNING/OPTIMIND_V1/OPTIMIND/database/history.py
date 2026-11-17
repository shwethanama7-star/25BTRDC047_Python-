import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path(__file__).resolve().parent / "optimind_history.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            event TEXT NOT NULL,
            detail TEXT NOT NULL
        )""")

def add_event(event, detail):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT INTO events(timestamp, event, detail) VALUES (?, ?, ?)",
                     (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), event, detail))

def get_events(limit=30):
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute(
            "SELECT timestamp, event, detail FROM events ORDER BY id DESC LIMIT ?",
            (limit,)
        ).fetchall()
