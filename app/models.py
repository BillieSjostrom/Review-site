from . import db


class Review(db.Model):
    """Review item."""
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.String(64))
    message = db.Column(db.String(256))

    def __repr__(self):
        return '<Review: {} - {}>'.format(self.id, self.movie)
