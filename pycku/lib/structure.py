from sqlalchemy import create_engine
from ..models import DBSession, Database
from sqlalchemy import MetaData

def get_db_engine(dbname):
    db = DBSession.query(Database).filter_by(db_name=dbname).first()
    if not db:
        return None

    conn_string = "{db_type}://{username}:{password}@{host}/{db_name}".format(
        db_type=db.db_type,
        username=db.db_user,
        password=db.db_pass,
        host=db.db_host,
        db_name=db.db_name)

    return create_engine(conn_string)


def get_tablenames(engine):
    return sorted(engine.table_names())

def get_table(t_name, engine):
    meta = MetaData(bind=engine)                                                                                                                                                
    meta.reflect()                                                                                                                                                                   
    return(meta.tables[t_name])                                                                                                                                        
