from flask import render_template
from app.main import mainbp as main
from app.main.forms import UserForm


@main.route('/')
def index():
    form = UserForm()
    return render_template('main/index.html', form=form)