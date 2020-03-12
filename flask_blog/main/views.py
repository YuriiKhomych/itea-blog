from flask import render_template, Blueprint

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('base.html', name="Name")
