import asyncio
from datetime import datetime
import os
import argparse
from src.db import create_database, connect, FILE_PATH
from src.object_detection import process_image
from src.services import update_task


parser = argparse.ArgumentParser()
parser.add_argument("--id")
args = parser.parse_args()
CONSUMER_ID = args.id
TIME_FORMAT = "%d/%m/%Y %H:%M:%S"
pending_tasks = []


async def check_tasks() -> None:
    global pending_tasks
    global CONSUMER_ID
    while True:
        await asyncio.sleep(5)
        conn, cur = connect()
        rows = list(
            cur.execute("SELECT id, file_name  FROM task WHERE status = 'pending'")
        )
        conn.close()
        pending_tasks_info = [
            (row[0], row[1])
            for row in rows
            if row[0] not in [el[0] for el in pending_tasks]
        ]
        if len(pending_tasks_info) > 0:
            time = datetime.now().strftime(TIME_FORMAT)
            print(f"[{time}] Consumer {CONSUMER_ID}: New tasks found!")
            pending_tasks += pending_tasks_info


async def consume_task():
    global pending_tasks
    while True:
        if len(pending_tasks) == 0:
            await asyncio.sleep(2)
            continue
        task_id = pending_tasks[0][0]
        file_name = pending_tasks[0][1]
        time = datetime.now().strftime(TIME_FORMAT)
        print(f"[{time}] Consumer {CONSUMER_ID}: Processing task...")
        pending_tasks = pending_tasks[1:]
        update_task(task_id=task_id, status="in_progress")
        num_of_people = process_image(file_name=file_name)
        update_task(task_id=task_id, status="done", num_of_people=num_of_people)
        time = datetime.now().strftime(TIME_FORMAT)
        print(f"[{time}] Consumer {CONSUMER_ID}: Task done!")


async def main() -> None:
    try:
        if not os.path.isfile(FILE_PATH):
            create_database()
        time = datetime.now().strftime(TIME_FORMAT)
        print(f"[{time}] Consumer {CONSUMER_ID}: Running...")
        await asyncio.gather(check_tasks(), consume_task())
    except asyncio.CancelledError:
        time = datetime.now().strftime(TIME_FORMAT)
        print(f"\n[{time}] Consumer {CONSUMER_ID}: Script stopped")


if __name__ == "__main__":
    pass
