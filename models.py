import os
from sqlalchemy import  create_engine
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import urllib.parse as up
import psycopg2

database_url= os.environ.get('DATABASE_URL')

db = SQLAlchemy()


def setup_db(app, database_path=database_url):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)
    # db.drop_all()
    db.create_all()


#many to many relation between Tag and Question
quistion_tag = db.Table('quistion_tag', db.Model.metadata,
      db.Column('quistion_id', db.Integer, db.ForeignKey('Question.id')),
      db.Column('tag_id', db.Integer, db.ForeignKey('Tag.id'))
)

# Question Table
class Question(db.Model):
    __tablename__ = 'Question'

    id = db.Column(db.Integer, primary_key=True)
    quistion_title = db.Column(db.String(120))
    answer = db.relationship('Answer', backref='Question', lazy = True)
    comments = db.relationship('Comment', backref='Question', lazy = True)
    following = db.relationship('Tag', secondary=quistion_tag, lazy='subquery',backref='followers')

    def __init__(self, quistion_title):
        self.quistion_title = quistion_title
     

    def format(self):
        return{
            'id': self.id,
            'quistion_title': self.quistion_title
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


# Answer Table
class Answer(db.Model):
    __tablename__ = 'Answer'

    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(120))
    comments = db.relationship('Comment', backref='Answer', lazy = True)
    quistion_id = db.Column(db.Integer, db.ForeignKey('Question.id'))

    def __init__(self, answer, quistion_id):
        self.answer = answer
        self.quistion_id = quistion_id

    def format(self):
        return {
            'id': self.id,
            'quistion_id':self.quistion_id,
            'answer': self.answer
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

# comment Table
class Comment(db.Model):
    __tablename__ = 'Comment'

    id = db.Column(db.Integer, primary_key=True)
    comment_title = db.Column(db.String(120))
    answer_id = db.Column(db.Integer, db.ForeignKey('Answer.id'))
    quistion_id = db.Column(db.Integer, db.ForeignKey('Question.id'))

    def __init__(self, comment_title, answer_id):
        self.comment_title = comment_title,
        self.answer_id = answer_id,

    def format(self):
        return {
            'id': self.id,
            'comment_title': self.comment_title,
            'answer_id': self.answer_id
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

# Tag Table
class Tag(db.Model):
    __tablename__ = 'Tag'

    id = db.Column(db.Integer, primary_key=True)
    tag_title = db.Column(db.String(120))


    def __init__(self, tag_title):
        self.tag_title = tag_title,

    def format(self):
        return {
            'id': self.id,
            'tag_title': self.tag_title,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()