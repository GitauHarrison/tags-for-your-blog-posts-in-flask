from flask import render_template, url_for, session, redirect
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        title='Post Something'
    )

@app.route('/blogs-by-tags')
def blogs_by_tags():
    return render_template(
        'blogs_by_tags.html',
        title='Blogs Based On'
    )
