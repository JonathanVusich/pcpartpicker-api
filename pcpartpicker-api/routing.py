from sanic import Sanic
from sanic.response import json
from sanic.response import HTTPResponse

app = Sanic.get_app()


@app.route('/<region:string>/<part:string>')
async def tag_handler(region: str, part: str) -> HTTPResponse:
    part_data = await get_database_request(region, part)
    return json(part_data)
