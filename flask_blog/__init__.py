from flask import Flask

from flask_blog.config import Configuration


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)

    from flask_blog.main.views import main

    app.register_blueprint(main)

    return app
