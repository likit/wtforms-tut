from flask import render_template, request
from app.main import mainbp as main
from app.main.forms import UserForm, EventForm


@main.route('/')
def index():
    form = UserForm()
    return render_template('main/index.html', form=form)


@main.route('/event/new', methods=['POST', 'GET'])
def create_event():
    form = EventForm()
    if request.method == 'POST':
        if form.add_location.data:
            form.locations.append_entry()
        elif all([form.remove_location.data,
                  len(form.locations.entries) > form.locations.min_entries]):
            entry = form.locations.pop_entry()
    return render_template('main/event.html', form=form)
