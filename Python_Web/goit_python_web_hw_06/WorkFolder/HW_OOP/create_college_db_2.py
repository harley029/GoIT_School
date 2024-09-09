from abc import ABC, abstractmethod
import os
import sqlite3


class DatabaseAdapter(ABC):
    @abstractmethod
    def execute_sql(self, sql: str) -> None:
        pass


class SQLiteDatabaseAdapter(DatabaseAdapter):
    def __init__(self, db_name: str):
        self.db_name = db_name

    def execute_sql(self, sql: str) -> None:
        try:
            with sqlite3.connect(self.db_name) as con:
                cur = con.cursor()
                cur.executescript(sql)
            print(f"Database '{self.db_name}' executed SQL successfully.")
        except sqlite3.Error as e:
            print(f"Error executing SQL: {e}")


class DatabaseCreator:
    def __init__(self, db_name: str, bd_tables: str, adapter: DatabaseAdapter):
        self.db_name = db_name
        self.bd_tables = bd_tables
        self.adapter = adapter

    def create_db(self):
        try:
            if self.bd_tables:
                with open(self.bd_tables, "r", encoding="UTF-8") as f:
                    sql = f.read()
                if self.db_name:
                    self.adapter.execute_sql(sql)
                    print(f"Database '{self.db_name}' created successfully.")
                else:
                    print("Database name is not set.")
            else:
                print("Cannot create database: No SQL file provided.")
        except Exception as e:
            print(f"Error creating database: {e}")


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

    db_adapter = SQLiteDatabaseAdapter(DB_NAME)
    db_creator = DatabaseCreator(DB_NAME, DB_TABLES, db_adapter)
    db_creator.create_db()

    # Uncomment the following lines to test database deletion
    # db_deleter = DatabaseDeleter(DB_NAME)
    # db_deleter.delete_db()
