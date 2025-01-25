import os
from flask import Flask


app = Flask(__name__)
app.config["SECRET_KEY"] = "e43c2e36583eae68c1a945b576f3561ebd4ef308e7f1928"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))[:-4]
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


if __name__ == "__main__":
    pass
