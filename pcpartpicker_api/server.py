from argparse import ArgumentParser

from sanic import Sanic, HTTPResponse, json, text

from .database import Database

parser = ArgumentParser(description="Sanic API for fetching cached pcpartpicker data.")
parser.add_argument("--database", type=str)
parser.add_argument("--host", type=str)
parser.add_argument("--port", type=int)
parser.add_argument("--access_log", type=bool)
args = parser.parse_args()

app = Sanic(name="pcpartpicker-api")
database = Database(args.database)


@app.get('/<region:string>/<part:string>')
async def tag_handler(request, region: str, part: str) -> HTTPResponse:
    parts = database.retrieve_items(region, part)
    return json(parts)


@app.get('/hello')
async def hello_handler(request) -> HTTPResponse:
    return text("Hello")


app.run(host=args.host, port=args.port, access_log=args.access_log)
