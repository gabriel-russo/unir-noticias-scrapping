from os.path import join
from sqlite3 import connect
from pandas import read_sql


class NewsDatabase:
    def __init__(self, db_path=".", db_name="database.db"):
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
        df.to_sql(
            name=table_name, con=self._conn, if_exists="replace", index_label="id"
        )

    def search(self, query):
        if "INSERT" in query.upper():
            raise Exception("Apenas buscas com SELECT são permitidas.")

        return read_sql(query, con=self._conn)

    def insert_difference(self, df, table_name):
        all_data = self.search(f"SELECT * FROM {table_name}")

        diff = df[~df["link"].isin(all_data["link"])]

        if not diff.empty:
            next_id = len(all_data) + 1
            for idx, row in diff.iterrows():
                self._conn.execute(
                    f"INSERT INTO {table_name} (id, title, link, date, viewed) VALUES (?, ?, ?, ?, ?);",
                    (next_id, row.title, row.link, row.date, "FALSE"),
                )
                self._conn.commit()
                next_id += 1
