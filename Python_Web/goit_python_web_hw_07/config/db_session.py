from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///college.db", echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

if __name__ == "__main__":
    pass
