from sqlite3 import Connection

from sanic import Sanic
from sanic.response import json
from sanic.response import HTTPResponse

from pcpartpicker.mappings import part_classes

app = Sanic.get_app()


@app.route('/<region:string>/<part:string>')
async def tag_handler(region: str, part: str) -> HTTPResponse:
    database: Connection = app.ctx.db[region]
    return json()
