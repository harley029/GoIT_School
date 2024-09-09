import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError


class DatabaseCreator:
    def __init__(self, db_name, bd_tables: str):
        self.db_name = db_name
        self.bd_tables = bd_tables

    def create_db(self):
        try:
            if self.bd_tables:
                with open(self.bd_tables, "r", encoding="UTF-8") as f:
                    sql_commands = f.read().split(";") # split SQL commands by ";"

                if self.db_name:
                    engine = create_engine(f"sqlite:///{self.db_name}", echo=False)
                    with engine.connect() as con:
                        for sql_command in sql_commands: # execute SQL commands one by one
                            con.execute(text(sql_command))
                    print(f"Database '{self.db_name}' created successfully.")
                else:
                    print("Database name is not set.")
            else:
                print("Cannot create database: No SQL file provided.")
        except FileNotFoundError:
            print(f"Error creating database: File '{self.bd_tables}' does not exist.")
        except SQLAlchemyError as e:
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

    db_creator = DatabaseCreator(DB_NAME, DB_TABLES)
    db_creator.create_db()

    # db_deleter = DatabaseDeleter(DB_NAME)
    # db_deleter.delete_db()

# 1. Створюємо об'єкт engine за допомогою create_engine функції SQLAlchemy.
# Цей об'єкт engine дозволяє нам з'єднатися з базою даних SQLite за допомогою SQLAlchemy.
# 2. Після того, як ми маємо об'єкт engine, ми викликаємо метод connect() для підключення до бази даних.
# 3. Потім ми виконуємо SQL-запити, що містяться у змінній sql, використовуючи метод execute() з параметром text(sql), що дозволяє виконати чистий SQL-код.
# 4. У SQLite можна виконувати лише один SQL-запит за раз.
#    4.1. У цьому випадку ми розділили SQL-код на окремі запити, розділені символом ;. Потім ми виконуємо кожен запит окремо в циклі for.
#    4.2. Метод con.execute() очікує об'єкт типу Executable, а не просто рядок SQL-коду.
#         Ми можемо використати клас text() з SQLAlchemy, щоб перетворити рядок на об'єкт, який може бути виконаний.
