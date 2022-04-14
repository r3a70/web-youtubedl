from sqlalchemy import Column, Integer, String
from backend.db.database import Base


class Visit(Base):
    __tablename__ = "visit"

    visited = Column(String, primary_key=True)


class Uses(Base):
    __tablename__ = "uses"

    downloaded = Column(Integer, primary_key=True)
    urls = Column(String)

