import sqlite3


class DatabaseReader:
    def __init__(self, database_name, database_location='./'):
        self.db_name = database_name
        self.db_loc = database_location
        self.table_names = list()

        self.setup()
        self.get_table_names()

    def setup(self):
        self.conn = sqlite3.connect(self.db_loc+self.db_name)
        self.cur = self.conn.cursor()

        data = self.cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table';")

        for datum in data:
            self.table_names.append(datum[0])

    def get_column_names_from_table(self, table_name):
        self.conn.row_factory = sqlite3.Row
        data = self.cur.execute(f" SELECT * FROM {table_name}")

        column_names = list()

        for datum in data.description:
            column_names.append(datum[0])

        self.conn.row_factory = None
        return column_names

    def get_table_names(self):
        return self.table_names



