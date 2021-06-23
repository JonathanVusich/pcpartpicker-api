from sanic import Sanic
from sanic.response import HTTPResponse
from sanic.response import json

from pcpartpicker_api.database import Database

app = Sanic.get_app()


@app.route('/<region:string>/<part:string>')
async def tag_handler(region: str, part: str) -> HTTPResponse:
    database: Database = app.ctx.db["database"]
    parts = database.retrieve_items(region, part)
    return json(parts)
