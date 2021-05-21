from sanic import Sanic
from pcpartpicker import API
import sqlite3

app = Sanic()
api = API()

app.ctx.db = {}

for region in api.supported_regions:
    app.ctx.db[region] = sqlite3.connect(f"/var/cache/pcpartpicker-api/{region}.db")

app.run()
