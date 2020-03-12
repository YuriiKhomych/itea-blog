from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_blog.config import Configuration

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)

    db.init_app(app)

    from flask_blog.main.views import main
    from flask_blog.posts.views import posts

    app.register_blueprint(main)
    app.register_blueprint(posts, url_prefix='/blog')

    return app
