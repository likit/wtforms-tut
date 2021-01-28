from app.main import mainbp as main


@main.route('/')
def index():
    return 'Index page'