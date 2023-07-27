from os.path import join
from sqlite3 import connect
from pandas import read_sql


class NewsDatabase:
    def __init__(self, db_path, db_name):
        self._path = db_path
        self._dbName = db_name
        self._conn = None

        self.__connect()

    def __connect(self):
        self._conn = connect(join(self._path, self._dbName))

    def disconnect(self):
        self._conn.close()
        self._conn = None

    def load_dataframe(self, df, table_name):
        df.to_sql(name=table_name, con=self._conn, if_exists="replace")

    def query(self, query):
        return read_sql(query, con=self._conn)
