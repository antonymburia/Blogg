from . import main
from flask_login import login_required,current_user
from flask import render_template,redirect,url_for,abort,request,flash
from ..models import User
from .. import db

#Views
@main.route('/', methods = ['GET','POST'])
def index():
    '''
    view to load index.html
    '''

    name = 'toni'

    return render_template('index.html',name = name)
    