from time import sleep
from flask import Blueprint, request
from src.config import app
from src.services import await_analysis_result, create_task, get_status
from src.utils import create_response, check_file_ext, save_image_from_url, save_image

API_ROUTES_BP = Blueprint("api_routes", __name__)


@app.route("/", methods=["GET"])
def api_endpoints():
    return {
        "GET": [
            "/api/read/file/<file_name> => Reads image from drive and computes people number",
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
    status = "pending"
    num_of_people = 0
    while status != "done":
        sleep(2)
        status, num_of_people = get_status(str(id))
    return create_response(id=id, status=status, num_of_people=int(num_of_people))


@app.route("/api/task/<string:id>", methods=["GET"])
def api_get_task_status(id):
    status, num_of_people = get_status(id)
    return create_response(id=int(id), status=status, num_of_people=int(num_of_people))


@app.route("/api/read/url", methods=["POST"])
def api_read_url_post():
    content_type = request.headers.get("Content-Type")
    url = (
        request.json["url"]
        if content_type == "application/json" and request.json
        else None
    )
    file_name = save_image_from_url(url=url) if url else None
    res = await_analysis_result(file_name=file_name)
    return res


@app.route("/api/upload", methods=["POST"])
def api_upload_file():
    if "file" not in request.files:
        return {"message": "No file provided"}
    file = request.files["file"]
    if file.filename == "":
        return {"message": "No selected file"}
    if not file or not check_file_ext(filename=file.filename):
        return {"message": "Invalid file provided"}
    file_name = save_image(file=file)
    res = await_analysis_result(file_name=file_name)
    return res


if __name__ == "__main__":
    pass
