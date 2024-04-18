from flask import render_template, request, url_for, flash, redirect, make_response
from app.actions import bp
from app.actions.forms import IntakeForm, CourtWatchForm
from app.models import States, CourtWatch, Counties, Orgs
from flask_login import login_required, current_user
from app.extensions import db
from datetime import datetime

@bp.route('/')
def index():
    return render_template('actions/index.html')

@bp.route('/intake/')
def intake():
    form = IntakeForm()
    return render_template('actions/intake.html', form=form)

@bp.route('/courtwatch', methods=('GET','POST'))
@login_required
def courtwatch():
    form = CourtWatchForm()
    form.county.choices = [("", "")]
    form.county.choices += [(item.id, item.county) for item in Counties.query.all()]
    form.states.choices = [("NY","NY")]
    uId = current_user.id
    if request.method == 'POST':
        new_report = CourtWatch(reportType="Grievance",submitterId=uId, judgeId=form.judgeId.data,
                            afcId=form.afcId.data,evaluatorId=form.evalId.data, opLawyerId=form.opLawyerId.data, effectedLawyerId= form.effectedLawyerId.data,
                            states=form.states.data, county=form.county.data, court=form.court.data, race=form.race.data, ethnicity=form.ethnicity.data,
                            gender=form.gender.data, highIncome=form.highIncome.data, highWealth=form.highWealth.data,
                            eighteenB=form.eighteenB.data, proSe=form.proSe.data, summary=form.summary.data, caseNum=form.caseNum.data)
        db.session.add(new_report)
        db.session.commit()
        return redirect(url_for('main.profile'))
    return render_template('actions/courtwatch.html', form=form)

@bp.route('/watchguide')
def watchguide():
    return render_template('actions/watchguide.html')