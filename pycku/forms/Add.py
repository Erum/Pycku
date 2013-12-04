from pyck.forms import Form
from wtforms import TextField, TextAreaField, validators


class addform(Form):
    name = TextField('Name', [validators.required("name cannot be empty")])
    Type= TextField('Type', [validators.required("type cannot be empty")])