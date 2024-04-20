from flask import Flask, render_template, request, url_for, flash, redirect, make_response
from app.claims import bp
from app.extensions import db
from app.claims.forms import ReportForm, AddActorForm, AddViolationForm, AddOrgForm, AddViolationsForm, AgreePublishForm
from app.models import States, Report, Actors, ActorType, Violations, VioCategory, ReportViolations, Counties, Orgs
from datetime import datetime
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import desc


@bp.route('/', methods=('GET','POST'))
def index():
    reports = Report.query.filter_by(published=1).order_by(Report.id.desc()).all()
    return render_template('claims/index.html', reports=reports)

@bp.route('/violations/<type>', methods=('GET','POST'))
@login_required
def entryViolations(type):
    type = type
    if type == 'grievance':
        pgTitle = "File a Grievance"
    else:
        pgTitle = "Report an Offender"
    return render_template('claims/violations.html', type=type, title=pgTitle)

#generic call that can be used for any forms using violations type
#vio_id is violations categories
@bp.route('/addviolations/<type>/<int:vio_id>', methods=('GET','POST'))
@login_required
def addViolations(type, vio_id):
    vId = vio_id
    type = type
    uId = current_user.id
    if type == 'grievance':
        pgTitle = "File a Grievance"
    else:
        pgTitle = "Report an Offender"
    vItem = vId - 1
    categories = VioCategory.query.all()
    category = categories[vItem]
    form = AddViolationsForm()
    form.violations.choices += [(item.id, item.violation) for item in Violations.query.filter_by(violationTypeId=vId).order_by('violationTypeId')]
    now = datetime.now()  # current date and time
    year = now.strftime("%Y")
    month = now.strftime("%m")
    if request.method == 'POST':
        # get userID and rID from session data {REMEMBER ADD THIS IN WHEN SESSIONS ADDED JUST DUMMY HERE!!!!!!}}
        record = Report.query.filter(Report.submitterId == uId).order_by(Report.id.desc()).first()
        rId =record.id
        record.summary = form.summary.data
        record.title = record.reportType[0]  + str(rId) + "_" + str(vId) + "_" + month + year + " " + category.category
        record.reportCategory = vId
        db.session.commit()

        for val in form.violations.data:
            new_violation = ReportViolations(reportId=rId, violationId=val)
            db.session.add(new_violation)
            db.session.commit()
        return redirect(url_for('claims.reviewReport', type=type, report_id=rId))

    return render_template('claims/addviolations.html', form=form, category=category, type=type, title=pgTitle)

@bp.route('/addreport/<type>', methods=('GET','POST'))
@login_required
def addReport(type):
    form = ReportForm(reportType = 'Report')
    type = type
    uId = current_user.id
    if type == 'grievance':
        pgTitle = "File a Grievance"
    else:
        pgTitle = "Report an Offender"
    #populate dynamic dropdowns
    form.badActorType.choices = [("","")]
    form.badActorType.choices += [(item.id, item.actorType) for item in ActorType.query.order_by('actorType')]
    form.county.choices = [("", "")]
    form.county.choices += [(item.id, item.county) for item in Counties.query.all()]
    form.states.choices = [("NY","NY")]
    if type == "report":
        del form.caseNum
    if request.method == 'POST':
        ## ADD IN GRABBING SUBMITTER ID FROM SESSION DATA WHEN SESSIONS SETUP> THIS JUST DUMMY HERE!!!!!!
        new_report = Report(reportType=form.reportType.data,submitterId = uId, badActorId =form.badActorId.data,
                            actorType=form.badActorType.data,states=form.states.data, county=form.county.data,
                            court=form.court.data, race=form.race.data, ethnicity=form.ethnicity.data,
                            gender=form.gender.data, highIncome=form.highIncome.data, highWealth=form.highWealth.data,
                            eighteenB=form.eighteenB.data, proSe=form.proSe.data)
        db.session.add(new_report)
        db.session.commit()
        return redirect(url_for('claims.entryViolations', type=type, title=pgTitle))
    return render_template('claims/addreport.html', form=form, type=type, title=pgTitle)


@bp.route('/reviewreport/<type>/<int:report_id>', methods=('GET','POST'))
@login_required
def reviewReport(type, report_id):
    form = AgreePublishForm(reportType='Report')
    # get userID from session data and find last report ID {REMEMBER ADD THIS IN WHEN SESSIONS ADDED JUST DUMMY HERE!!!!!!}}
    rId = report_id
    uId = current_user.id
    print(uId)
    type = type
    if type == 'grievance':
        pgTitle = "File a Grievance"
    else:
        pgTitle = "Report an Offender"
    report = Report.query.filter(Report.submitterId == uId).order_by(Report.id.desc()).first()
    violations = ReportViolations.query.filter(ReportViolations.reportId == rId).all()
    if request.method == 'POST':
        report.published = form.publishAgree.data
        db.session.commit()
        print('made it here')
        return render_template('claims/nextsteps.html', type=type, id=rId, title=pgTitle)
    if type == 'grievance':
        return render_template('claims/reviewgrievance.html', id=rId, report=report, violations=violations, type=type, title=pgTitle, form=form)
    if type == 'report':
        return render_template('claims/reviewreport.html', id=rId, report=report, violations=violations, type=type, title=pgTitle, form=form)


@bp.route('/reviewgrievance/<type>/<int:report_id>', methods=('GET','POST'))
@login_required
def reviewGrievance(type, report_id):
    rId = report_id
    uId = current_user.id
    type=type
    report = Report.query.filter(Report.submitterId == uId).order_by(Report.id.desc()).first()
    violations = ReportViolations.query.filter(ReportViolations.reportId == rId).all()

    return render_template('claims/reviewgrievance.html', type=type, report=report, violations = violations, id=rId)

@bp.route('/viewreport/<int:report_id>', methods=('GET','POST'))
def viewReport(report_id):
    # get userID from session data and find last report ID {REMEMBER ADD THIS IN WHEN SESSIONS ADDED JUST DUMMY HERE!!!!!!}}
    rId = report_id
    report = Report.query.filter(Report.id == rId).order_by(Report.id.desc()).first()
    violations = ReportViolations.query.filter(ReportViolations.reportId == rId).all()
    return render_template('claims/viewreport.html', report=report, violations = violations)

@bp.route('/viewgrievance/<int:report_id>', methods=('GET','POST'))
def viewGrievance(report_id):
    # get userID from session data and find last report ID {REMEMBER ADD THIS IN WHEN SESSIONS ADDED JUST DUMMY HERE!!!!!!}}
    rId = report_id
    report = Report.query.filter(Report.submitterId == rId).order_by(Report.id.desc()).first()
    violations = ReportViolations.query.filter(ReportViolations.reportId == rId).all()
    return render_template('claims/viewgrievance.html', report=report, violations = violations)

# admin interface to add violation to list of all
@bp.route('/nextsteps/<type>/<int:report_id>', methods=('GET','POST'))
@login_required
def nextSteps(type,report_id):
    type=type
    if type == 'grievance':
        pgTitle = "File a Grievance"
    else:
        pgTitle = "Report an Offender"
    rId = report_id
    return render_template('claims/nextsteps.html', type=type, id=rId, title=pgTitle)

# admin interface to add violation to list of all
@bp.route('/addviolation/', methods=('GET','POST'))
@login_required
def addViolation():
    form = AddViolationForm()
    if request.method == 'POST':
        new_violation = Violations(violation=form.violation.data,violationTypeId=form.violationTypeId.data)
        db.session.add(new_violation)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('claims/addviolation.html', form=form)

@bp.route('/addactor/', methods=('GET','POST'))
@login_required
def addActor():
    actors = ActorType.query.all()
    form = AddActorForm()
    if request.method == 'POST':
        new_actor = Actors(fName=form.fName.data,lName=form.lName.data,FUID=form.FUID.data,licenseNum=form.licenseNum.data, email=form.email.data)
        db.session.add(new_actor)
        db.session.commit()
        return redirect(url_for('claims.addReport', type='report'))
    return render_template('claims/addactor.html', form=form, actors=actors)

@bp.route('/addorg/', methods=('GET','POST'))
@login_required
def addOrg():
    form = AddOrgForm()
    form.states.choices = [("","")]
    form.states.choices += [(item.abbrv, item.abbrv) for item in States.query.all()]
    if request.method == 'POST':
        new_org = Orgs(name=form.name.data,address1=form.address1.data,address2=form.address2.data,  city=form.city.data,state=form.states.data,zipcode=form.zipcode.data,phone=form.phone.data, orgEmail=form.orgEmail.data,website=form.website.data )
        db.session.add(new_org)
        db.session.commit()
        #get originating type from session data {{{ADD THIS IN ONE SESSIONS SET}}}
        type='Grievance'
        if type == 'Report':
            return redirect(url_for('claims.addReport'))
        if type == 'Grievance':
            return redirect(url_for('claims.addGrievance'))
        else:
            return redirect(url_for('main.index'))
    return render_template('claims/addorg.html', form=form)
