from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class BlogForm(FlaskForm):
    blog_content = StringField('blog content',validators=[DataRequired()])
    submit = SubmitField('Submit')
