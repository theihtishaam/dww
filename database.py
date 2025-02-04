# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, convert_unicode=True, echo=False)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def init_db():
    import models
    models.Base.metadata.create_all(bind=engine)
