from flask import  redirect, render_template, url_for, current_app
from . import main
from .. import db
from ..models import Review
from .forms import ReviewForm


@main.route('/', methods=['GET', 'POST'])
def index():
    """Default application route."""
    form = ReviewForm()
    if form.validate_on_submit():
        current_app.logger.debug('Form validated ok.')
        review=Review(movie=form.movie.data, message=form.message.data)
        db.session.add(review)
        db.session.commit()
        current_app.logger.debug('Added new review ({}).'.format(review))
        return redirect(url_for('main.index'))

    reviews = db.session.query(Review).all()
    return render_template('index.html', reviews=reviews, form=form)


@main.route('/remove/<int:id>')
def remove(id):
    review= Review.query.get(id)
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for('main.index'))
