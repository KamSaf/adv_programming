import asyncio
import os
import argparse
from src.db import create_database, connect, FILE_PATH
from src.object_detection import process_image
from src.services import update_task
from src.utils import log

parser = argparse.ArgumentParser()
parser.add_argument("--id")
args = parser.parse_args()
CONSUMER_ID = args.id
if CONSUMER_ID is None:
    print("No Consumer ID provided!")
    exit()

pending_tasks = []
TASK_LIMIT = 2


async def check_tasks() -> None:
    global pending_tasks
    global CONSUMER_ID
    await asyncio.sleep(2)
    conn, cur = connect()
    rows = list(
        cur.execute(
            f"SELECT id, file_name  FROM task WHERE status = 'pending' LIMIT {TASK_LIMIT}"
        )
    )
    conn.close()
    pending_tasks_info = [
        (row[0], row[1])
        for row in rows
        if row[0] not in [el[0] for el in pending_tasks]
    ]
    if len(pending_tasks_info) > 0:
        for task in pending_tasks_info:
            update_task(task_id=task[0], status="in_progress")
        log(message="New tasks found!", consumer_id=CONSUMER_ID)
        pending_tasks += pending_tasks_info


async def consume_task():
    global pending_tasks
    if len(pending_tasks):
        task_id = pending_tasks[0][0]
        file_name = pending_tasks[0][1]
        log(message=f"Processing task {task_id}...", consumer_id=CONSUMER_ID)
        pending_tasks = pending_tasks[1:]
        num_of_people = process_image(file_name=file_name)
        update_task(task_id=task_id, status="done", num_of_people=num_of_people)
        log(message="Task done!", consumer_id=CONSUMER_ID)


async def main() -> None:
    try:
        if not os.path.isfile(FILE_PATH):
            create_database()
        log(message="Running...", consumer_id=CONSUMER_ID)
        while True:
            await asyncio.gather(check_tasks(), consume_task())
    except (asyncio.CancelledError, KeyboardInterrupt):
        log(message="Script stopped", consumer_id=CONSUMER_ID)


if __name__ == "__main__":
    pass
