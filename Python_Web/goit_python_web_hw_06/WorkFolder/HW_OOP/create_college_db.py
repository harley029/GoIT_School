import os
import sqlite3


class DatabaseCretor:

    def __init__(self, db_name, bd_tables: str):
        self._db_name = None
        self._bd_tables = None
        self.db_name = db_name
        self.bd_tables = bd_tables

    @property
    def db_name(self):
        return self._db_name

    @property
    def bd_tables(self):
        return self._bd_tables

    @db_name.setter
    def db_name(self, db_name):
        if os.path.exists(db_name):
            self._db_name = db_name
        else:
            print(f"File '{db_name}' does not exist. Will be created.")
            self._db_name = db_name

    @bd_tables.setter
    def bd_tables(self, bd_tables):
        if os.path.exists(bd_tables):
            self._bd_tables = bd_tables
        else:
            print(f"File '{bd_tables}' does not exist.")
            self._bd_tables = None

    def create_db(self):
        try:
            if self.bd_tables:  # Перевірка, чи не є bd_tables рівним None
                with open(self.bd_tables, "r", encoding="UTF-8") as f:
                    sql = f.read()
                if self.db_name:
                    with sqlite3.connect(self.db_name) as con:
                        cur = con.cursor()
                        cur.executescript(sql)
                    print(f"Database '{self.db_name}' created successfully.")
                else:
                    print("Database name is not set.")
            else:
                print("Cannot create database: No SQL file provided.")
        except sqlite3.Error as e:
            print(f"Error creating database: {e}")
        except FileNotFoundError:
            print(f"Error creating database: File '{self.bd_tables}' does not exist.")


class DatabaseDeletor:

    def __init__(self, db_name):
        self._db_name = None
        self.db_name = db_name

    @property
    def db_name(self):
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        if os.path.exists(db_name):
            self._db_name = db_name
        else:
            print(f"Database '{db_name}' does not exist. ")
            self._db_name = None

    def delete_db(self):
        if self.db_name:
            os.remove(self.db_name)
            print(f"Database '{self.db_name}' deleted successfully.")


if __name__ == "__main__":
    db_name = "college.db"
    db_еtables = "college.sql"

    db_creator = DatabaseCretor(db_name, db_еtables)
    db_creator.create_db()

    # db_deleter = DatabaseDeletor(db_name)
    # db_deleter.delete_db()