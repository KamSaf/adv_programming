import time
import requests
from src.db import connect
from src.config import ROOT_DIR


def create_task(file_name: str) -> int:
    conn, cur = connect()
    cur.execute(
        "INSERT INTO task (file_name, status) VALUES (:file_name, :status)",
        {"file_name": file_name, "status": "pending"},
    )
    data = list(cur.execute("SELECT id FROM task ORDER BY id DESC LIMIT 1;"))[0][0]
    conn.commit()
    print("\n✅ New task created!")
    conn.close()
    return data


def get_status(id: str) -> str:
    conn, cur = connect()
    id = list(
        cur.execute("SELECT status, num_of_people FROM task WHERE id = :id", {"id": id})
    )[0]
    conn.close()
    return id


def save_image(url: str) -> str | None:
    response = requests.head(url)
    content_type = response.headers.get("Content-Type")
    if content_type and content_type.startswith("image/"):
        ext = content_type.split("/")[-1]
    else:
        return None
    try:
        img_data = requests.get(url).content
    except Exception:
        return None
    file_name = f"{str(time.time()).replace('.', '')}.{ext}"
    file_path = f"{ROOT_DIR}/images/{file_name}"
    with open(file_path, "wb") as handler:
        handler.write(img_data)
    return file_name


def update_task(task_id: int, status: str, num_of_people: int | None = None) -> None:
    conn, cur = connect()
    if num_of_people:
        cur.execute(
            "UPDATE task SET status = :status, num_of_people = :num_of_people WHERE id = :id",
            {"status": status, "num_of_people": num_of_people, "id": task_id},
        )
    else:
        cur.execute(
            "UPDATE task SET status = :status WHERE id = :id",
            {"status": status, "id": task_id},
        )
    conn.commit()
    conn.close()


def create_response(id: int, status: str, num_of_people: int) -> dict:
    response = (
        {
            "task_id": id,
            "task_status": status,
            "num_of_people": num_of_people,
        }
        if num_of_people
        else {
            "task_id": id,
            "task_status": status,
        }
    )
    return response


if __name__ == "__main__":
    pass
