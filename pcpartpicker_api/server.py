from argparse import ArgumentParser

from sanic import Sanic, HTTPResponse, json

from .database import Database

parser = ArgumentParser(description="Sanic API for fetching cached pcpartpicker data.")
parser.add_argument("--database", type=str)
parser.add_argument("--host", type=str)
parser.add_argument("--port", type=int)
args = parser.parse_args()

app = Sanic(name="pcpartpicker-api")
database = Database(args.database)


@app.get('/<region:string>/<part:string>')
async def tag_handler(region: str, part: str) -> HTTPResponse:
    parts = database.retrieve_items(region, part)
    return json(parts)


app.run(host=args.host, port=args.port)
