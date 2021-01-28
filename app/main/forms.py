import arrow
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms_alchemy import ModelForm as ModelAlchemyForm
from wtforms_alchemy import model_form_factory, ModelFieldList
from wtforms import FormField
from app import db
from app.main.models import User, Event, Location
from wtforms_components.fields import EmailField

BaseModelForm = model_form_factory(FlaskForm)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(cls):
        return db.session


class UserForm(ModelForm):
    class Meta:
        model = User
        email = EmailField()


class LocationForm(ModelAlchemyForm):
    class Meta:
        model = Location


class EventForm(ModelForm):
    class Meta:
        model = Event
        field_args = {'start_at': {'default': arrow.get(datetime.today())}}
        date_format = '%d/%m/%Y'
    locations = ModelFieldList(FormField(LocationForm), min_entries=5, max_entries=5)
