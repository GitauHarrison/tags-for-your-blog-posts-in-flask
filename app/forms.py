from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class BlogForm(FlaskForm):
    """Form to add a blog post"""
    username = StringField(
        'Username', validators=[DataRequired()], render_kw={"placeholder": "muthoni"})
    email = StringField(
        'Email', validators=[DataRequired(), Email()], 
        render_kw={"placeholder": "muthoni@email.com"})
    body = TextAreaField(
        'Body',
        validators=[DataRequired(), Length(min=0, max=140)],
        render_kw={"placeholder": "Say something ..."})
    tags = SelectMultipleField(
        'Tag Name',
        validators=[DataRequired()],
        choices=[
            ('Python', 'Python'),
            ('Flask', 'Flask'),
            ('Database', 'Database')
        ])
    submit = SubmitField('Post')
