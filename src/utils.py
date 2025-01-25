import time
import requests
from src.config import ROOT_DIR
from src.config import ALLOWED_EXTENSIONS
from werkzeug.datastructures import FileStorage


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


def save_image_from_url(url: str) -> str | None:
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


def save_image(file: FileStorage) -> str | None:
    if not file.filename:
        return None
    ext = file.filename.rsplit(".", 1)[-1].lower()
    file_name = f"{str(time.time()).replace('.', '')}.{ext}"
    file_path = f"{ROOT_DIR}/images/{file_name}"
    file.save(file_path)
    return file_name


def check_file_ext(filename: str | None) -> bool:
    return (
        "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
        if filename
        else False
    )


if __name__ == "__main__":
    pass
