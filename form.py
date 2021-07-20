from wtforms import Form, StringField, SelectField
from wtforms.fields.simple import SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

ENGINES = ('All', 'Hybrid', 'Petrol', 'Electric', 'Diesel')
MODEL = ('All', 'BMW', 'Lada', 'Opel')


class CarSearchForm(Form):
    csrf = True

    model = SelectField(label="model", choices=MODEL)
    engine = SelectField(label='Engine', choices=ENGINES)
    submit = SubmitField('Submit')
