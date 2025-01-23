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
    id = list(cur.execute("SELECT status FROM task WHERE id = :id", {"id": id}))[0][0]
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
    file_name = f"{ROOT_DIR}/images/{str(time.time()).replace('.', '')}.{ext}"
    with open(file_name, "wb") as handler:
        handler.write(img_data)
    return file_name


if __name__ == "__main__":
    pass
