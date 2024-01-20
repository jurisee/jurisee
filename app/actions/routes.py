from flask import render_template
from app.actions import bp
from app.actions.forms import IntakeForm


@bp.route('/')
def index():
    return render_template('actions/index.html')

@bp.route('/intake/')
def intake():
    form = IntakeForm()
    return render_template('actions/intake.html', form=form)