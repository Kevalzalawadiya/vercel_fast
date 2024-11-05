from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@localhost/user_management"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://jatinpadmani1:adminadmin@jatinpadmani1.mysql.pythonanywhere-services.com/jatinpadmani1$default"         

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
