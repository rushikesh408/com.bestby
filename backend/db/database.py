from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

db_engine = create_engine(DATABASE_URL)

Dblocalsession = sessionmaker(autocommit=False, bind=db_engine)

Base = declarative_base()


def get_db():
    db_session = Dblocalsession()
    try:
        yield db_session
    finally:
        db_session.close()
