from app import app, db
from app.models import Tag, Post, User


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Tag=Tag, Post=Post, User=User)
