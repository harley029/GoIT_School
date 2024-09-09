from sqlalchemy import Boolean, create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from db import Base, engine


class Owner(Base):
    __tablename__ = "owners"
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(150))
    email = Column(String(150), unique=True)

class Cat(Base):
    __tablename__ = "cats"
    id = Column(Integer, primary_key=True)
    nick = Column(String(50))
    age = Column(Integer)
    vacinated = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("owners.id"), nullable=True)
    owner = relationship("Owner", backref="cats")

Base.metadata.create_all(bind=engine)
