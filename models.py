import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, DateTime

# --------------------------------------------
# CONFIG
# --------------------------------------------

if 'DATABASE_URL' not in os.environ:
  database_name = "casting"
  database_path = "postgres://{}:{}@{}/{}".format('postgres','rammel','localhost:5432', database_name)
else:
  database_path = "postgres://xziznhghlbhwox:250ea74c53494d88192282efc13e6676da8b73faba05544ccb97206ba2f55381@ec2-54-156-149-189.compute-1.amazonaws.com:5432/d1mqqn6tjiljlh"

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app

    db.init_app(app)
    db.create_all()


# --------------------------------------------
# MODELS
# --------------------------------------------

class Actors(db.Model):  
  __tablename__ = 'Actors'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(Integer)
  gender = Column(String)

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
  
  # def __repr__(self):
  #   return 'This is the __repr__ method of Actors table'

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender
    }

class Movies(db.Model):  
  __tablename__ = 'Movies'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  release = Column(DateTime)

  def __init__(self, title, release):
    self.title = title
    self.release = release

  def __repr__(self):
    return 'This is the __repr__ method of Movies table'

  def insert(self):
    db.session.add(self)
    db.session.commit()
    
  def update(self):
    self.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release': self.release
  }
