from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection URL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:password@hostname/dbname"

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models
Base = declarative_base()
