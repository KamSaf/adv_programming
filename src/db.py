import os.path
import sqlite3
from src.config import ROOT_DIR

FILE_PATH = f"{ROOT_DIR}/queue.db"


def connect() -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    conn = sqlite3.connect(FILE_PATH)
    return (conn, conn.cursor())


def create_database() -> None:
    if os.path.isfile(FILE_PATH):
        return
    conn, cur = connect()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS task
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT,
            status TEXT,
            num_of_people INTEGER DEFAULT 0
        )
        """
    )
    conn.commit()
    print("\n✅ Database file created!")
    conn.close()


if __name__ == "__main__":
    pass
