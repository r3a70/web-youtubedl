from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


POSTGRESQL_DATABASE_URL = os.environ.get("POSTGRESQL_DATABASE_URL")  # "postgresql://user:password@postgresserver/db"

engine = create_engine(
    POSTGRESQL_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


