from app import db
from datetime import datetime
from hashlib import md5


tags_table = db.Table(
    'tags_associatioon',
    db.Column('post_id', db.ForeignKey('post.id'), primary_key=True),
    db.Column('tag_id', db.ForeignKey('tag.id'), primary_key=True),
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'User: {self.username}'

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    tags = db.relationship(
        'Tag',
        secondary=tags_table,
        backref=db.backref('post', lazy='dynamic'))

    def __repr__(self):
        return f'Post {self.title}'


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return f'Tag: {self.name}'
