import os

from config.db_models import Base

from sqlalchemy import create_engine

# Видаляєм існуючу базу данних
if os.path.exists("college.db"):
    os.remove("college.db")

# Створюємо зʼєднання з базою данних
URI = f"sqlite:///college.db"
engine = create_engine(URI, echo=False)

# Створюємо новий файл з базой данних
Base.metadata.create_all(engine)

if __name__ == "__main__":
    pass
