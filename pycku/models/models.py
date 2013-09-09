from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    )

from . import DBSession, Base


class Database(Base):
    __tablename__ = 'databases'

    id = Column(Integer, primary_key=True)
    descriptive_name = Column(Unicode(200), unique=True)
    db_name = Column(Unicode(200)) 
    db_user = Column(Unicode(200))
    db_pass = Column(Unicode(200))
    db_host = Column(Unicode(200))
    db_type= Column(Unicode(200))

