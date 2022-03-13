from . import main
from flask_login import login_required,current_user
from flask import render_template,redirect,url_for,abort,request,flash
from ..models import User
from .. import db
from ..request import get_quotes

#Views
@main.route('/', methods = ['GET','POST'])
def index():
    '''
    view to load index.html
    '''

    quote = get_quotes()

    return render_template('index.html',quote = quote)
    

@main.route('/user/<usersname>')
def profile(usersname):
    user = User.query.filter_by(username = usersname).first()
    user_joined = user.date_joined.strftime('%b %d, %Y')


    if user is None:
        abort(404)
        

    

    return render_template("profile/profile.html", user = user, date = user_joined)