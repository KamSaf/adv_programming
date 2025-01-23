import asyncio
import os
from src.db import create_database, connect, FILE_PATH
from src.object_detection import process_image
from src.services import update_task

pending_tasks = []


async def check_tasks() -> None:
    global pending_tasks
    while True:
        await asyncio.sleep(5)
        conn, cur = connect()
        rows = list(
            cur.execute("SELECT id, file_name  FROM task WHERE status = 'pending'")
        )
        pending_tasks_info = [
            (row[0], row[1])
            for row in rows
            if row[0] not in [el[0] for el in pending_tasks]
        ]
        if len(pending_tasks_info) > 0:
            print("New tasks found!")
            pending_tasks += pending_tasks_info
        conn.close()


async def consume_task():
    global pending_tasks
    while True:
        if len(pending_tasks) == 0:
            await asyncio.sleep(2)
            continue
        task_id = pending_tasks[0][0]
        file_name = pending_tasks[0][1]
        print("Processing task...")
        pending_tasks = pending_tasks[1:]
        update_task(task_id=task_id, status="in_progress")
        num_of_people = process_image(file_name=file_name)
        update_task(task_id=task_id, status="done", num_of_people=num_of_people)
        print("Task done!")


async def main() -> None:
    try:
        if not os.path.isfile(FILE_PATH):
            create_database()
        print("Running...")
        await asyncio.gather(check_tasks(), consume_task())
    except asyncio.CancelledError:
        print("\nScript stopped")


if __name__ == "__main__":
    pass
