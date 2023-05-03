# Tags For Your Blog Posts

![Tags System](/app/static/images/tags_system.gif)

Add tags to your blog posts. Find blog posts based on your tags.

## Technologies Used

- Tailwind CSS for styling and cross-browser responsiveness
- Flask-migrate
- Flask-sqlalchemy
- SQLite

## Features

- User data saved to a database
- Data filter using tags

## Testing 

**Demo: [On render](https://tags-system-flask.onrender.com)**

- Clone this repo:

    ```python
    $ git clone git@github.com:GitauHarrison/tags-for-your-blog-posts-in-flask.git
    ```

- Change directory to the cloned repo:

    ```python
    $ cd tags-for-your-blog-posts-in-flask
    ```

- Create and activate your virtualenvironemnt:

    ```python
    $ mkvirtualenv venv # I am using virtualenvwrapper
    ```

- Install project dependancies:

    ```python
    (venv)$ pip3 install -r requirements.txt
    ```

- Update your environment variables:

    ```python
    (venv)$ cp .env-template .env
    ```

- Start your Flask server:

    ```python
    (venv)$ flask run
    ```

- Paste your localhost link in your browser to see the application's GUI.

## Reference:

- [Add tags to your Flask blog posts](https://github.com/GitauHarrison/notes/blob/master/tags_flask_blog_posts.md)