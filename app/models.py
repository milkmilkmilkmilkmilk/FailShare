from datetime import datetime

from .extensions import db


class Post(db.Model):
    """Post model representing a failure share entry."""

    id = db.Column(db.Integer, primary_key=True)
    failure_text = db.Column(db.Text, nullable=False)
    cause_text = db.Column(db.Text, nullable=False)
    suggestion_text = db.Column(db.Text, nullable=True)
    detail_text = db.Column(db.Text, nullable=True)
    tags_csv = db.Column(db.String(255), nullable=False)
    image_path = db.Column(db.String(512), nullable=True)
    locale = db.Column(db.String(8), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Post id={self.id} locale={self.locale}>"

