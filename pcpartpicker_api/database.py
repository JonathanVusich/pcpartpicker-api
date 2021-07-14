import sqlite3

from typing import List


class Database:

    def __init__(self, database: str):
        self._connection = sqlite3.connect(database)

    def retrieve_items(self, region: str, part_type: str) -> List[str]:
        cursor = self._connection.cursor()
        cursor.execute(f'select * from {region}_{part_type}')
        return cursor.fetchall()
