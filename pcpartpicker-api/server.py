from sanic import Sanic
from pcpartpicker import API
from litedb import DiskDatabase

app = Sanic()
api = API()

app.ctx.db = {}

for region in api.supported_regions:
    app.ctx.db[region] = DiskDatabase(f"/var/cache/pcpartpicker-api/{region}")

app.run()
