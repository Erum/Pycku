
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from sqlalchemy import create_engine
from ..models import (
    DBSession,Database
    )

from ..forms import ContactForm


@view_config(route_name='home', renderer='home.mako')
def my_view(request):
    one = None
    return {'one': one, 'project': 'pycku'}


@view_config(route_name='contact', renderer="contact.mako")
def contact_form(request):

    f = ContactForm(request.POST)   # empty form initializes if not a POST request

    if 'POST' == request.method and 'form.submitted' in request.params:
        if f.validate():
            #TODO: Do email sending here.

            request.session.flash("Your message has been sent!")
            return HTTPFound(location=request.route_url('home'))

    return {'contact_form': f}

@view_config(route_name='insert', renderer='insert.mako')
def insert(request):
    one = None
    return {'one': one, 'project': 'pycku'}
    
    
@view_config(route_name='structure', renderer='structure.mako')
def structure(request):
    one = None
    
    username = 'iram'
    password = 'beenish'
    host = 'localhost'
    database = 'abc'
    db_type = 'mysql'
    #conn_string = "mysql://pycku:pheonixix@localhost/database".format(db_type=db_type, username=username, password=password, host=host, database=database)
    #conn_string
    #'mysql://pycku:pheonix@localhost/database'
    conn_string = "mysql://iram:beenish@localhost/abc"
    engine = create_engine(conn_string)
    tables = engine.table_names()
    return {'one': one, 'project': 'pycku', tables: tables}