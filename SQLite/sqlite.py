#
# Author: Rohtash Lakra
#
import sqlite3
from typing import Any, Union


class SQLiteManager:
    """SQLite Manager"""

    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.cursor = None

    def connect(self):
        # In-Memory Database
        # conn = sqlite3.connect(':memory:')
        # Physical Database
        self.conn = sqlite3.connect(self.db_file)
        self.conn.row_factory = sqlite3.Row

        # Init Cursor
        self.cursor = self.conn.cursor()

    def commit(self, onlyCursor: bool = False):
        self.cursor.execute('commit')
        if not onlyCursor:
            self.conn.commit()

    def disconnect(self):
        self.cursor.close()
        self.conn.close()
        self.conn = None
        self.cursor = None

    def execute(self, query: str, params: Union[Any, None] = None, many: bool = False):
        """Executes Query"""
        if many:
            self.cursor.executemany(query)
        elif params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)

    def fetch_all(self):
        # return self.cursor.keys()
        # print(self.cursor.description)
        results = self.cursor.fetchall()
        results = [dict(row) for row in results]
        return results


db_name = 'test.db'
sqlite = SQLiteManager(db_name)
sqlite.connect()


class UserManager():

    def __init__(self):
        # Create User's Table
        create_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            status TEXT
        )
        """
        sqlite.execute(create_table)

    def add_user(self, first_name, last_name, email, status):
        insert_query = """
        INSERT INTO users (first_name, last_name, email, status)
        VALUES (?, ?, ?, ?)
        """
        sqlite.execute(insert_query, (first_name, last_name, email, status))

    def get_users(self):
        select_query = """
        SELECT * FROM users
        """
        sqlite.execute(select_query)
        return sqlite.fetch_all()


userManager = UserManager()
userManager.add_user('Roh', 'Lak', 'roh@lak.com', 'active')

users = userManager.get_users()
print(f"Users: {len(users)}")
print(f"Users: {users}")

# Disconnect DB
sqlite.disconnect()
