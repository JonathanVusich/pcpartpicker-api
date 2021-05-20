from sanic import Sanic
from sanic.response import json
from sanic.response import HTTPResponse
from litedb import DiskDatabase

from pcpartpicker.mappings import part_classes

app = Sanic.get_app()


@app.route('/<region:string>/<part:string>')
async def tag_handler(region: str, part: str) -> HTTPResponse:
    database: DiskDatabase = app.ctx.db[region]
    part_data = [item for item in database.select(part_classes[part])]
    return json(part_data)
