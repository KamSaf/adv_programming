from flask import Blueprint, request
from src.config import app
from src.services import create_task
from src.utils import save_image_from_url

API_ROUTES_BP = Blueprint("api_alt_routes", __name__)


@app.route("/alt", methods=["GET"])
def api_endpoints_alt():
    return {
        "GET": [
            "/api_alt/read/file/<file_name> => Reads image from drive and returns task ID",
        ],
        "POST": [
            "/api_alt/upload => Receives POST request containing image and returns task ID",
            "/api_alt/read/url => Reads image from URL and returns task ID",
        ],
    }


@app.route("/api_alt/read/file/<string:file_name>", methods=["GET"])
def api_read_file_alt(file_name):
    id = create_task(file_name=file_name)
    return {"message": "New task created", "task_id": id}


@app.route("/api_alt/read/url", methods=["POST"])
def api_read_url_post_alt():
    content_type = request.headers.get("Content-Type")
    url = (
        request.json["url"]
        if content_type == "application/json" and request.json
        else None
    )
    file_name = save_image_from_url(url) if url else None
    id = create_task(file_name) if file_name else None
    message = "New task created" if id else "Invalid data provided"
    return {"message": message, "task_id": id}


@app.route("/api_alt/upload", methods=["POST"])
def api_upload_file_alt():
    return {"message": "work in progess.."}


if __name__ == "__main__":
    pass
