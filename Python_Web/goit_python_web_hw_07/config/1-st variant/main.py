from create_db_alchemy import DatabaseCreator

if __name__ == "__main__":

    DB_NAME = "college.db"
    DB_TABLES = "college.sql"

    db_creator = DatabaseCreator(DB_NAME, DB_TABLES)
    db_creator.create_db()
