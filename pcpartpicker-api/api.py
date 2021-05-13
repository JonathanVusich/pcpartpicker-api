from flask import Flask, g
from litedb import DiskDatabase

app = Flask(__name__)

DATABASE_PATH = "/path/to/database.db"

DATABASE = DiskDatabase(DATABASE_PATH)


@app.route("/<region>/<part>")
def retrieve_data(region: str, part: str) -> str:
    return ""
