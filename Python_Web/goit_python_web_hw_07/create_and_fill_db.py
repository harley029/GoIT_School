''' SQLite database via SQLAlchemy '''

from config.db_create import Base
from config.db_session import session
from seed import fill_in_db, DB_NAME

if __name__ == "__main__":
    pass
    # ------------------------------------ Створити файл з базою данних ---------------------------
    db_creator = Base
    db_creator()

    # ------------------------------------ Заповнити базу данних згенерованими данними ------------
    db_data_importer=fill_in_db
    db_data_importer(DB_NAME, session)