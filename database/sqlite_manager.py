import sqlite3
from pathlib import Path


class SQLiteManager:
    """
    Administra la conexión SQLite de la aplicación.
    """

    def __init__(self):

        database_path = (
            Path("database") /
            "wetracking_rfid.db"
        )

        self._connection = sqlite3.connect(
            database_path
        )

    @property
    def connection(self):

        return self._connection

    def close(self):

        self._connection.close()