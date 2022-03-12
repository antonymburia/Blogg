from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from . import login_manager


class User(UserMixin,db.Model):
  __tablename__ = 'users'
  id =db.Column(db.Integer,primary_key =True)
  username = db.Column(db.String(255),index = True)
  firstname = db.Column(db.String(255))
  lastname = db.Column(db.String(255))
  email = db.Column(db.String(255),unique = True,index = True)
  bio = db.Column(db.String(1000))
  profile_pic_path = db.Column(db.String)
  pass_secure = db.Column(db.String(255))
  date_joined = db.Column(db.DateTime,default=datetime.utcnow)


  @property
  def password(self):
    raise AttributeError('The password is private')

  @password.setter
  def password(self,password):
    self.pass_secure = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)


  def __repr__(self):
    return f'User {self.username}'

  @login_manager.user_loader
  def load_user(user_id):
    return User.query.get(int(user_id))