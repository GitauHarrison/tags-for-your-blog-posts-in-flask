from flask import render_template, url_for, redirect, request, flash
from app.forms import PostForm
from app.models import Tag, Post, User
from app import app, db


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if request.method == 'POST':
        user = User(username=form.username.data, email=form.email.data)
        post = Post(body=form.body.data, title=form.title.data, author=user)
        for tag in form.tags.data:
            post.tags.append(Tag(name=tag))
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Post saved')
        return redirect(url_for('index'))

    # Get all posts
    all_blogs = len(Post.query.all())
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)

    # Pagination
    next_url = url_for('index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template(
        'index.html',
        title='Post Something',
        form=form,
        posts=posts.items,
        all_blogs=all_blogs,
        next_url=next_url,
        prev_url=prev_url)


@app.route('/tag: <name>')
def tag(name):
    posts_by_tag = len(Tag.query.filter_by(name=name).all())
    page = request.args.get('page', 1, type=int)
    tags = Tag.query.filter_by(name=name).order_by(
        Tag.timestamp.desc()).paginate(
            page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('tag', name=name, page=tags.next_num) \
        if tags.has_next else None
    prev_url = url_for('tag', name=name, page=tags.prev_num) \
        if tags.has_prev else None
    return render_template(
        'tags.html',
        title=f'Posts Related To {name}',
        posts_by_tag=posts_by_tag,
        tags=tags.items,
        next_url=next_url,
        prev_url=prev_url)
