
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
    return {'one': one, 'project': 'pycku'}
username = 'pycku'
password = 'pheonix'
host = 'localhost'
database = 'database'
db_type = 'mySQL'
conn_string = "mySQL://pycku:pheonix@localhost/database".format(db_type=db_type, username=username, password=password, host=host, database=database)
conn_string
'mySQL://pycku:pheonix@localhost/database'
engine = create_engine(conn_string)
engine.table_names()
[u'database']
