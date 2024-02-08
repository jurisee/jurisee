from flask import Flask, render_template, request, url_for, flash, redirect, make_response
from app.registry import bp
from app.extensions import db
from app.registry.forms import ReportForm, AddActorForm, AddViolationForm, AddOrgForm, AddViolationsForm
from app.models import States, Report, Actors, ActorType, Violations, VioCategory, ReportViolations, Counties, Orgs
from datetime import datetime
from sqlalchemy import desc


@bp.route('/', methods=('GET','POST'))
def index():
    reports = Report.query.order_by(Report.id.desc()).all()
    return render_template('registry/index.html', reports=reports)

@bp.route('/violations/<type>', methods=('GET','POST'))
def entryViolations(type):
    type = type
    if type == 'grievance':
        pgTitle = "File a Grievance"
    else:
        pgTitle = "Report an Offender"
    return render_template('registry/violations.html', type=type, title=pgTitle)

#generic call that can be used for any forms using violations type
#vio_id is violations categories
@bp.route('/addviolations/<type>/<int:vio_id>', methods=('GET','POST'))
def addViolations(type, vio_id):
    vId = vio_id
    type = type
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
        uId = 3
        record = Report.query.filter(Report.submitterId == 3).order_by(Report.id.desc()).first()
        rId =record.id
        record.summary = form.summary.data
        record.title = record.reportType[0]  + str(rId) + "_" + str(vId) + "_" + month + year + " " + category.category
        record.vioCategoryId = vId
        db.session.commit()

        for val in form.violations.data:
            new_violation = ReportViolations(reportId=rId, violationId=val)
            db.session.add(new_violation)
            db.session.commit()
        return redirect(url_for('registry.reviewReport', type=type, report_id=rId))

    return render_template('registry/addviolations.html', form=form, category=category, type=type, title=pgTitle)

@bp.route('/addreport/<type>', methods=('GET','POST'))
def addReport(type):
    form = ReportForm(reportType = 'Report')
    type = type
    if type == 'grievance':
        pgTitle = "File a Grievance"
    else:
        pgTitle = "Report an Offender"
    #populate dynamic dropdowns
    form.badActorType.choices = [("","")]
    form.badActorType.choices += [(item.id, item.actorType) for item in ActorType.query.order_by('actorType')]
    form.county.choices = [("", "")]
    form.county.choices += [(item.id, item.county) for item in Counties.query.all()]
    form.states.choices = [("32","NY")]
    if type == "report":
        del form.caseNum
    if request.method == 'POST':
        ## ADD IN GRABBING SUBMITTER ID FROM SESSION DATA WHEN SESSIONS SETUP> THIS JUST DUMMY HERE!!!!!!
        new_report = Report(reportType=form.reportType.data,submitterId = 3, badActorId =form.badActorId.data, actorType=form.badActorType.data,states=form.states.data, county=form.county.data,court=form.court.data)
        db.session.add(new_report)
        db.session.commit()
        return redirect(url_for('registry.entryViolations', type=type, title=pgTitle))
    return render_template('registry/addreport.html', form=form, type=type, title=pgTitle)


@bp.route('/reviewreport/<type>/<int:report_id>', methods=('GET','POST'))
def reviewReport(type, report_id):
    # get userID from session data and find last report ID {REMEMBER ADD THIS IN WHEN SESSIONS ADDED JUST DUMMY HERE!!!!!!}}
    rId = report_id
    uId = 3
    type = type
    if type == 'grievance':
        pgTitle = "File a Grievance"
    else:
        pgTitle = "Report an Offender"
    report = Report.query.filter(Report.submitterId == 3).order_by(Report.id.desc()).first()
    violations = ReportViolations.query.filter(ReportViolations.reportId == rId).all()
    print(violations)
    if type == 'grievance':
        return render_template('registry/reviewgrievance.html', id=rId, report=report, violations=violations, type=type, title=pgTitle)
    if type == 'report':
        return render_template('registry/reviewreport.html', id=rId, report=report, violations=violations, type=type, title=pgTitle)

@bp.route('/reviewgrievance/<type>/<int:report_id>', methods=('GET','POST'))
def reviewGrievance(type, report_id):
    # get userID from session data and find last report ID {REMEMBER ADD THIS IN WHEN SESSIONS ADDED JUST DUMMY HERE!!!!!!}}
    rId = report_id
    uId = 3
    type=type
    report = Report.query.filter(Report.submitterId == 3).order_by(Report.id.desc()).first()
    violations = ReportViolations.query.filter(ReportViolations.reportId == rId).all()
    print(violations)

    return render_template('registry/reviewgrievance.html', type=type, report=report, violations = violations, id=rId)

@bp.route('/viewreport/<int:report_id>', methods=('GET','POST'))
def viewReport(report_id):
    # get userID from session data and find last report ID {REMEMBER ADD THIS IN WHEN SESSIONS ADDED JUST DUMMY HERE!!!!!!}}
    rId = report_id
    uId = 3
    report = Report.query.filter(Report.submitterId == 3).order_by(Report.id.desc()).first()
    violations = ReportViolations.query.filter(ReportViolations.reportId == rId).all()
    return render_template('registry/viewreport.html', report=report, violations = violations)

@bp.route('/viewgrievance/<int:report_id>', methods=('GET','POST'))
def viewGrievance(report_id):
    # get userID from session data and find last report ID {REMEMBER ADD THIS IN WHEN SESSIONS ADDED JUST DUMMY HERE!!!!!!}}
    rId = report_id
    uId = 3
    report = Report.query.filter(Report.submitterId == 3).order_by(Report.id.desc()).first()
    violations = ReportViolations.query.filter(ReportViolations.reportId == rId).all()
    return render_template('registry/viewgrievance.html', report=report, violations = violations)

# admin interface to add violation to list of all
@bp.route('/nextsteps/<type>/<int:report_id>', methods=('GET','POST'))
def nextSteps(type,report_id):
    type=type
    if type == 'grievance':
        pgTitle = "File a Grievance"
    else:
        pgTitle = "Report an Offender"
    rId = report_id
    return render_template('registry/nextsteps.html', type=type, id=rId, title=pgTitle)

# admin interface to add violation to list of all
@bp.route('/addviolation/', methods=('GET','POST'))
def addViolation():
    form = AddViolationForm()
    if request.method == 'POST':
        new_violation = Violations(violation=form.violation.data,violationTypeId=form.violationTypeId.data)
        db.session.add(new_violation)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('registry/addviolation.html', form=form)

@bp.route('/addactor/', methods=('GET','POST'))
def addActor():
    actors = ActorType.query.all()
    form = AddActorForm()
    if request.method == 'POST':
        new_actor = Actors(fName=form.fName.data,lName=form.lName.data,FUID=form.FUID.data,licenseNum=form.licenseNum.data, email=form.email.data)
        db.session.add(new_actor)
        db.session.commit()
        return redirect(url_for('registry.addOrg'))
    return render_template('registry/addactor.html', form=form, actors=actors)

@bp.route('/addorg/', methods=('GET','POST'))
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
            return redirect(url_for('registry.addReport'))
        if type == 'Grievance':
            return redirect(url_for('registry.addGrievance'))
        else:
            return redirect(url_for('main.index'))
    return render_template('registry/addorg.html', form=form)
