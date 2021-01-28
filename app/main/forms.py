import arrow
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from app import db
from app.main.models import User, Event
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


class EventForm(ModelForm):
    class Meta:
        model = Event
        field_args = {'start_at': {'default': arrow.get(datetime.today())}}
        date_format = '%d/%m/%Y'
