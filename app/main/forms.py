from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class BlogForm(FlaskForm):
    blog_title = StringField('blog title',validators=[DataRequired()])
    blog_content = StringField('blog content',validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('leave a comment below:',validators=[DataRequired()])
    submit = SubmitField('comment')