import sqlite3
from src.utils import create_database, FILE_PATH

DEFAULT_TASK_NAME = "do something"


def create_task(task_name: str = DEFAULT_TASK_NAME) -> None:
    conn = sqlite3.connect(FILE_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO task (task_name, status) VALUES (:task_name, :status)",
        {"task_name": task_name, "status": "pending"},
    )
    conn.commit()
    print("\n✅ New task created!")
    conn.close()


if __name__ == "__main__":
    create_database()
    create_task()
