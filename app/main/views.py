from . import main
from flask_login import login_required,current_user
from flask import render_template,redirect,url_for,abort,request,flash
from ..models import User,Blog
from .. import db
from ..request import get_quotes

#Views
@main.route('/', methods = ['GET','POST'])
def index():
    '''
    view to load index.html
    '''

    quote = get_quotes()

    blogs = Blog.query.all()
  

    return render_template('index.html',quote = quote, blogs = blogs)
    

@main.route('/user/<usersname>')
def profile(usersname):
    user = User.query.filter_by(username = usersname).first()
    user_joined = user.date_joined.strftime('%b %d, %Y')


    if user is None:
        abort(404)
        

    

    return render_template("profile/profile.html", user = user, date = user_joined)

@main.route('/blog/new', methods = ['GET','POST'])
@login_required
def new_blog():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        blog_content = blog_form.blog_content.data
        blog = blog_form.blog_content.data
        category = blog_form.category.data

        # Updated blog instance
        new_blog = Blog(blog_content=blog_content,user=current_user)

        # Save blog method
        new_blog.save_blog()
        return redirect(url_for('.index'))

    
    return render_template('newblog.html',blog_form = blog_form )