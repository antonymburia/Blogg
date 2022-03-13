from . import main
from flask_login import login_required,current_user
from flask import render_template,redirect,url_for,abort,request,flash
from ..models import User,Blog,Comment
from .. import db
from ..request import get_quotes
from .forms import BlogForm, CommentForm

#Views
@main.route('/', methods = ['GET','POST'])
def index():
    '''
    view to load index.html
    '''

    quote = get_quotes()

    user = User.query.filter_by(username = current_user.username).first()
   

    blogs = Blog.query.all()
    
  

    return render_template('index.html',quote = quote, blogs = blogs, name = user)
    

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
        blog_title = blog_form.blog_title.data
        blog_content = blog_form.blog_content.data
        
    
        # Updated blog instance
        new_blog = Blog(blog_title = blog_title, blog_content=blog_content,user=current_user)

        # Save blog method
        new_blog.save_blog()
        return redirect(url_for('.index'))

    
    return render_template('newblog.html',blog_form = blog_form )

@main.route('/blog/<id>', methods = ['GET','POST'])
def blogs(id):

    '''
    View root page function that returns the blog page and its data
    '''

    blogs = Blog.query.filter_by(id=id).first()
    blog = Blog.query.filter_by(id=blogs.id).first()
    blog_id = blog.id
    comments = Comment.get_comments(blog)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data
        new_comment = Comment(comment = comment,user = current_user, blog = blog_id)
        new_comment.save_comment()
        
        flash('Your comment has been submitted')
    
    
    return render_template('blog.html', blogs = blogs, comment_form = comment_form, comments = comments)
