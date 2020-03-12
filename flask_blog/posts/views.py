from flask import Blueprint, request, current_app, redirect, url_for
from flask import render_template

from flask_blog import db
from flask_blog.posts.models import Post, Tag
from posts.forms import PostForm

posts = Blueprint('posts', __name__, template_folder='templates')


#http://localhost/blog/create
@posts.route('/create', methods=["GET", "POST"])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            current_app.logger.exception('Something wrong')
            # kibana, sentry

        return redirect(url_for('posts.index'))
    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/')
def index():
    all_posts = Post.query.all()
    return render_template('posts/index.html', posts=all_posts)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


# http://localhost/blog/tag/python
@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)
