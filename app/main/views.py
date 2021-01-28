from flask import render_template
from app.main import mainbp as main
from app.main.forms import UserForm, EventForm


@main.route('/')
def index():
    form = UserForm()
    return render_template('main/index.html', form=form)


@main.route('/event/new')
def create_event():
    form = EventForm()
    return render_template('main/event.html', form=form)
