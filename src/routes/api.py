from flask import Blueprint
from src.config import app

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


@app.route("/api/read/file", methods=["GET"])
def api_read_file():
    return {"message": "work in progess.."}


@app.route("/api/read/url", methods=["GET", "POST"])
def api_read_url():
    return {"message": "work in progess.."}


@app.route("/api/task/status", methods=["GET"])
def api_get_task_status():
    return {"message": "work in progess.."}


@app.route("/api/upload", methods=["POST"])
def api_upload_file():
    return {"message": "work in progess.."}


if __name__ == "__main__":
    pass
