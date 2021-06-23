from sanic import Sanic

from database import Database

app = Sanic()

app.ctx.db = {"database", Database("/var/cache/pcpartpicker-api.db")}

app.run()
