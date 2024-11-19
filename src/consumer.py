from pathlib import Path
import asyncio

FILE_PATH = "queue.txt"
pending_tasks = []


async def check_tasks() -> None:
    global pending_tasks
    while True:
        await asyncio.sleep(5)
        # print("looking for new tasks...")
        with open(FILE_PATH, "r") as file:
            for line in file:
                split_line = line.split("|")
                if (
                    split_line[-1].strip() == "pending"
                    and int(split_line[0]) - 1 not in pending_tasks
                ):
                    print("new task found!")
                    pending_tasks.append(int(split_line[0]) - 1)


def update_task_status(task_id: int, status: str) -> None:
    with open(FILE_PATH, "r") as file:
        file_data = file.readlines()
    new_line = file_data[task_id].split("|")
    new_line[2] = f" {status}"
    file_data[task_id] = "|".join(new_line) + "\n"
    with open(FILE_PATH, "w") as file:
        file.writelines(file_data)


async def consume_task() -> None:
    global pending_tasks
    while True:
        if len(pending_tasks) == 0:
            await asyncio.sleep(2)
            continue
        task_id = pending_tasks[0]
        print("doing task...")
        pending_tasks = pending_tasks[1:]
        update_task_status(task_id=task_id, status="in_progress")
        await asyncio.sleep(30)
        update_task_status(task_id=task_id, status="done")
        print("task done!")


async def main() -> None:
    Path(FILE_PATH).touch(exist_ok=True)
    print("running...")
    await asyncio.gather(check_tasks(), consume_task())


if __name__ == "__main__":
    asyncio.run(main())
