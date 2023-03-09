import sqlite3


class Database:
    """
    Класс для подключения к базе данных, создания таблицы
    и добавления данных от пользователя
    """

    def __init__(self, db_file):
        self.con = sqlite3.connect(db_file)
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS appointments
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              date DATETIME,
              time TIMESTAMP,
              phone TEXT)"""
        self.cur.execute(query)
        self.con.commit()

    def add_reservation(self, name, date, time, phone):
        self.cur.execute("""INSERT INTO appointments (name, date, time, phone) VALUES (?, ?, ?, ?)""",
                         (name, date, time, phone))
        self.con.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.cur.close()
        self.con.close()
        if exc_value:
            raise
