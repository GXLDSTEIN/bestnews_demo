from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    author = db.Column(db.String, nullable=True)
    source = db.Column(db.String, nullable=True)

    def __repr__(self):
        return "<News {} {}".format(self.title, self.created_at)
