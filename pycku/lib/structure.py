from sqlalchemy import create_engine
from ..models import DBSession, Database
#username = 'pycku'
#password = 'pheonix'
#host = 'localhost'
#database = 'database'
#db_type = 'mySQL'
#conn_string = "mySQL://pycku:pheonix@localhost/database".format(db_type=db_type, username=username, password=password, host=host, database=database)
#conn_string
#'mySQL://pycku:pheonix@localhost/database'
#engine = create_engine(conn_string)
#engine.table_names()
#[u'database']


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
