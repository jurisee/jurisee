from flask import render_template
from app.actions import bp
from app.actions.forms import IntakeForm, CourtWatchForm


@bp.route('/')
def index():
    return render_template('actions/index.html')

@bp.route('/intake/')
def intake():
    form = IntakeForm()
    return render_template('actions/intake.html', form=form)

@bp.route('/courtwatch')
def courtwatch():
    form = CourtWatchForm()
    return render_template('actions/courtwatcher.html', form=form)