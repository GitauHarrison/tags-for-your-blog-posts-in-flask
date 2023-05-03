import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    # Web form
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-cannot-guess'

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.dirname(__file__), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Pagination
    POSTS_PER_PAGE = int(os.environ.get('POSTS_PER_PAGE'))

    # Logs
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
