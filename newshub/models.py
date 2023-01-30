from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# adding configuration for using a sqlite database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
app.app_context().push()

migrate = Migrate(app, db)

# initialize the app with the extension
db.init_app(app)

class Daily(db.Model):
    __tablename__ = 'daily'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable = True)
    language = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    newses = db.relationship("News",backref = "daily",lazy=True)



    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __repr__(self):
        return self.name

class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    content = db.Column(db.String)
    image = db.Column(db.String, nullable = True)
    daily_id = db.Column(db.Integer,db.ForeignKey("daily.id"))

    def __repr__(self):
        return self.title

#db.create_all()