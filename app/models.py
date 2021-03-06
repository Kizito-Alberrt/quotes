from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager

# Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quote:
    '''
    Class That defines the quote object
    '''

    def __init__(self, id, author, quote):
        self.id = id
        self.author = author
        self.quote = quote

class User(UserMixin, db.Model):
    '''
    db.Model connects our class to our database
    Args:
        gives tables in our database proper names
    ''' 
    
    __tablename__ = 'users' 
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True, unique = True)
    email = db.Column(db.String(255), unique = True, index = True)
    password_hash = db.Column(db.String(155))
    image_file = db.Column(db.String(255), nullable = False, default = 'default.jpg')
    blog = db.relationship('Blog', backref = 'user', lazy = 'dynamic')
    comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def password(s):
        '''
        Raises an attribute error when we try to access the password
        '''
        raise AttributeError('You cannot read the password attribute') 

    @password.setter
    def password(self, password):
            self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
            return check_password_hash(self.password_hash, password)

    def __repr__(self):
        '''
        Defines how the user object will be constructed when the class is called
        '''
        return f'User{self.username}'

class Blog(UserMixin, db.Model):

    __tablename__ = 'blogs'

    id  = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    postedDate = db.Column(db.DateTime, default = datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog = db.relationship('Comment', backref = 'user_blog', lazy = 'dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()
class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text())
    postedDate = db.Column(db.DateTime, default = datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, blog_id):
        '''
        Takes in blo and retrieves all comments for that blog
        '''
        comments = Comment.query.filter_by(blog_id = blog_id).all()
        return comments

    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()