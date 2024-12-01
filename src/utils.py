import os.path
import sqlite3

FILE_PATH = "queue.db"


def create_database() -> None:
    if os.path.isfile(FILE_PATH):
        return
    conn = sqlite3.connect(FILE_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS task
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT,
            status TEXT
        )
        """
    )
    conn.commit()
    print("\n✅ Database file created!")
    conn.close()


def print_tasks():
    conn = sqlite3.connect(FILE_PATH)
    cur = conn.cursor()
    print(list(cur.execute("SELECT * FROM task")))
    conn.close()


if __name__ == "__main__":
    pass
