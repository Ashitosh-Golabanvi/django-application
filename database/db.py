# database/db.py

import sqlite3
from pathlib import Path

# Set the path to the SQLite database (same as in settings.py)
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db.sqlite3"

def get_connection():
    """Establishes and returns a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Allows accessing rows as dictionaries
    return conn

def initialize_db():
    """Initializes the database and creates the users table if it doesn't exist."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()
