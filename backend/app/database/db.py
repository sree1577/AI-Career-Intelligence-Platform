from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/career_platform")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Each model class will inherit from this Base
Base = declarative_base()

# Session factory — used to talk to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
