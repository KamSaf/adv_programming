from flask import Blueprint, request
from src.config import app
from src.services import create_task, get_status, save_image

API_ROUTES_BP = Blueprint("api_routes", __name__)


@app.route("/", methods=["GET"])
def api_endpoints():
    return {
        "GET": [
            "/api/read/file/<file_name> => Reads image from drive and computes people number",
            "/api/read/url/<url_to_image> => Reads image from URL and computes people number",
            "/api/task/status/<task_id> => Returns task status",
        ],
        "POST": [
            "/api/upload => Receives POST request containing image and computes people number",
            "/api/read/url => Reads image from URL and computes people number",
        ],
    }


@app.route("/api/read/file/<string:file_name>", methods=["GET"])
def api_read_file(file_name):
    id = create_task(file_name=file_name)
    return {"message": "New task created", "task_id": id}


@app.route("/api/read/url/<string:url_to_image>", methods=["GET"])
def api_read_url(url_to_image):
    # ????????????????????
    return {"message": url_to_image}


@app.route("/api/read/url", methods=["POST"])
def api_read_url_post():
    content_type = request.headers.get("Content-Type")
    url = (
        request.json["url"]
        if content_type == "application/json" and request.json
        else None
    )
    file_name = save_image(url) if url else None
    id = create_task(file_name) if file_name else None
    message = "New task created" if id else "Invalid data provided"
    return {"message": message, "task_id": id}


@app.route("/api/task/<string:id>", methods=["GET"])
def api_get_task_status(id):
    status = get_status(id)
    return {"task_id": int(id), "task_status": status}


@app.route("/api/upload", methods=["POST"])
def api_upload_file():
    return {"message": "work in progess.."}


if __name__ == "__main__":
    pass
