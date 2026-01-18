import os
import sqlite3
from pathlib import Path

DEFAULT_DB = "data/tickets.db"

def get_db_path() -> Path:
    return Path(os.getenv("TICKET_SQLITE_PATH", DEFAULT_DB))

def connect() -> sqlite3.Connection:
    db_path = get_db_path()
    db_path.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db() -> None:
    with connect() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            impact INTEGER NOT NULL,
            urgency INTEGER NOT NULL,
            priority TEXT NOT NULL,
            "group" TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        """)
        conn.commit()