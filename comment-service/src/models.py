from flask_sqlalchemy import SQLAlchemy
from src.app import db
from datetime import datetime

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, nullable=False)  # Reference to blog post
    user_id = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, post_id, user_id, text):
        self.post_id = post_id
        self.user_id = user_id
        self.text = text