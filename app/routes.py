from flask import render_template, url_for, redirect, request
from app.forms import BlogForm
from app.models import Tag, Post, User
from app import app, db


@app.route('/')
@app.route('/index')
def index():
    form = BlogForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        blog = Post(body=form.body.data, author=user.username)
        for tag in form.tags.data:
            blog.tags.append(Tag(name=tag))
        db.session.add(user)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('home'))
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num) \
        if posts.has_prev else None
    all_blogs = len(Post.query.all())
    return render_template(
        'index.html',
        title='Post Something',
        form=form,
        posts=posts.items,
        all_blogs=all_blogs,
        next_url=next_url,
        prev_url=prev_url)


@app.route('/blogs-by-tags')
def blogs_by_tags():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('blogs_by_tags', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('blogs_by_tags', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template(
        'blogs_by_tags.html',
        title='Blogs Based On',
        posts=posts.items,
        next_url=next_url,
        prev_url=prev_url)
