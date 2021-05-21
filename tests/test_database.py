from pcpartpicker_api.database import Database
from pcpartpicker.parts import CFM


def test_database():
    database = Database('sqlite://')
    session = database.create_session()
    session.add(CFM(0, 10, 4))
    session.commit()

