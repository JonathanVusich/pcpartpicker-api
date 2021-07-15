import sqlite3

from typing import List

from pcpartpicker import API


class Database:

    def __init__(self, database: str):
        self._connection = sqlite3.connect(database)
        self._api = API()

    def retrieve_items(self, region: str, part_type: str) -> List[str]:
        if region in self._api.supported_regions and part_type in self._api.supported_parts:
            cursor = self._connection.cursor()
            cursor.execute(f'select * from {region}_{part_type}')
            return cursor.fetchall()
        return []
