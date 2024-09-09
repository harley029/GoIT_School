import os
import sqlite3


class DatabaseCreator:
    def __init__(self, db_name, bd_tables: str):
        self.db_name = db_name
        self.bd_tables = bd_tables

    def create_db(self):
        try:
            if self.bd_tables:
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


class DatabaseDeleter:
    def __init__(self, db_name):
        self.db_name = db_name

    def delete_db(self):
        try:
            if os.path.exists(self.db_name):
                os.remove(self.db_name)
                print(f"Database '{self.db_name}' deleted successfully.")
            else:
                print(f"Database '{self.db_name}' does not exist.")
        except Exception as e:
            print(f"Error deleting database: {e}")


if __name__ == "__main__":
    DB_NAME = "college.db"
    DB_TABLES = "college.sql"

    db_creator = DatabaseCreator(DB_NAME, DB_TABLES)
    db_creator.create_db()

    # db_deleter = DatabaseDeleter(DB_NAME)
    # db_deleter.delete_db()
