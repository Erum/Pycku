
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from sqlalchemy import create_engine
from ..models import (
    DBSession,Database
    )
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    )

from ..forms import ContactForm,addform
from ..lib import structure

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
#@view_config(route_name='addcol', renderer="add.mako")
#def Add_form(request):

#   f = AddForm(request.POST)   # empty form initializes if not a POST request

#   if 'POST' == request.method and 'form.submitted' in request.params:
#       if f.validate():
           
  #         request.session.flash("Column has been created")
  #         return HTTPFound(location=request.route_url('manage_table',dbname=db,tablename=t))

 #  return {'Add_form': f} 


#@view_config(route_name='insert', renderer='insert.mako')
#def insert(request):
 #   one = None
  #  return {'one': one, 'project': 'pycku'}


@view_config(route_name='manage_db', renderer='managedb.mako')
def manage_db(request):
    dbname = request.matchdict['dbname']
    engine = structure.get_db_engine(dbname)
    tablenames = structure.get_tablenames(engine)

    return {'dbname': dbname, 'tablenames': tablenames, 'db_engine': engine}


@view_config(route_name='manage_table', renderer='managetable.mako')
def manage_table(request):
    dbname = request.matchdict['dbname']
    tablename = request.matchdict['tablename']
    engine = structure.get_db_engine(dbname)
    tablenames = structure.get_tablenames(engine)
    table = structure.get_table(tablename, engine)

    return {'dbname': dbname, 'tablenames': tablenames, 'db_engine': engine,
            'table': table}
            
            
@view_config(route_name='addcol', renderer='add.mako')
def addcol(request):
    dbname = request.matchdict['dbname']
    tablename = request.matchdict['tablename']
    engine = structure.get_db_engine(dbname)
    tablenames = structure.get_tablenames(engine)
    table = structure.get_table(tablename, engine)
    #column=Column('new column',string(100))
    if 'POST' == request.method:
        column=Column('new column', Unicode(100))
        #table.append(column)

    return {'dbname': dbname, 'tablenames': tablenames, 'db_engine': engine,
            'table': table, 'tablename': tablename}

@view_config(route_name='structure', renderer='structure.mako')
def structure_view(request):
    e=structure.get_db_engine(dbname) 
    tnames=structure.get_tablenames(e)
    t=structure.get_table(t_name, engine)
    return {'dbname': dbname,'db_engine': e,'tablenames':tnames}
