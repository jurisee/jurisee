from flask import Flask, render_template, request, url_for, flash, redirect, make_response
from app.registry import bp
from app.extensions import db
from app.registry.forms import ReportForm, AddActorForm, AddViolationForm, AddOrgForm, AddViolationsForm
from app.models import Report, Actors, ActorType, VioCategory, Violations, ReportViolations, ViolationsSum, States, Counties, Orgs
import json
from sqlalchemy import func


@bp.route('/', methods=('GET','POST'))
def index():
    reports = Report.query.all()
    return render_template('registry/index.html', reports=reports)

@bp.route('/violations/', methods=('GET','POST'))
def entryViolations():
    return render_template('registry/violations.html')

#generic call that can be used for any forms using violations type
#vio_id is violations categories
@bp.route('/addviolations/<int:vio_id>', methods=('GET','POST'))
def addViolations(vio_id):
    vId = vio_id
    vItem = vId - 1
    categories = VioCategory.query.all()
    count = VioCategory.query.count()
    category = categories[vItem]
    form = AddViolationsForm()
    form.violations.choices += [(item.id, item.violation) for item in Violations.query.filter_by(violationTypeId=vId).order_by('violationTypeId')]

    if request.method == 'POST':
        # get live from session data to determine if new report needed {{REMEMBER ADD THIS IN WHEN SESSIONS ADDED JUST DUMMY HERE!!!!!!}}
        live = 1
        # get userID from session data and find last report ID {REMEMBER ADD THIS IN WHEN SESSIONS ADDED JUST DUMMY HERE!!!!!!}}
        uId = 3
        report = Report.query.filter(Report.submitterId == uId).order_by(Report.date_created.desc()).first()
        reportId = report.id
        if live == 1:
            #create new_report w gen info from last report
            new_report = Report(reportType=report.reportType, title=report.title, submitterId=uId,
                                summary= report.summary, caseNum= report.caseNum,
                                badActorId=report.badActorId, badActorType= report.badActorType,
                                states= report.states, county= report.county, court= report.court)
            db.session.add(new_report)
            db.session.flush()
            reportId = new_report.id
            db.session.commit()
        else:
            live = 1
            #session['live'] = live {{REMMEBER TO CHANGE THIS TO SESSION DATE WHEN SETUP
        for val in form.violations.data:
            new_violation = ReportViolations(reportId=reportId, violationId=val)
            db.session.add(new_violation)
            db.session.commit()
        if vId < count:
            next = vId + 1
            return redirect(url_for('registry.addViolations', vio_id=next))
        else:
            return redirect(url_for('registry.entryViolations'))

    return render_template('registry/addviolations.html', form=form, category=category)

@bp.route('/addreport/', methods=('GET','POST'))
def addReport():
    form = ReportForm(reportType = 'Report')
    #populate dynamic dropdowns
    form.badActorType.choices = [("","")]
    form.badActorType.choices += [(item.id, item.actorType) for item in ActorType.query.order_by('actorType')]
    form.badActorType.choices += [("Other", "Other")]
    form.states.choices = [("","")]
    form.states.choices += [(item.abbrv, item.abbrv) for item in States.query.all()]
    if request.method == 'POST':
        ## ADD IN GRABBING SUBMITTER ID FROM SESSION DATA WHEN SESSIONS SETUP> THIS JUST DUMMY HERE!!!!!!
        new_report = Report(reportType=form.reportType.data,title=form.title.data, submitterId = 3, summary=form.summary.data,  hideSummary=form.hideSummary.data, caseNum=form.caseNum.data,badActorId =form.badActorId.data,badActorType=form.badActorType.data,states=form.states.data, county=form.county.data,court=form.court.data)
        db.session.add(new_report)
        db.session.commit()
        return redirect(url_for('registry.entryViolations'))
    return render_template('registry/addreport.html', form=form)

@bp.route('/addgrievance/', methods=('GET','POST'))
def addGrievance():
    form = ReportForm(reportType = 'Grievance')
    #populate dynamic dropdowns
    form.badActorType.choices = [("","")]
    form.badActorType.choices += [(item.id, item.actorType) for item in ActorType.query.order_by('actorType')]
    form.badActorType.choices += [("Other", "Other")]
    form.states.choices = [("","")]
    form.states.choices += [(item.abbrv, item.abbrv) for item in States.query.all()]
    if request.method == 'POST':
        ## ADD IN GRABBING SUBMITTER ID FROM SESSION DATA WHEN SESSIONS SETUP> THIS JUST DUMMY HERE!!!!!!
        new_report = Report(reportType=form.reportType.data,title=form.title.data, submitterId = 3, summary=form.summary.data,  hideSummary=form.hideSummary.data, caseNum=form.caseNum.data,badActorId =form.badActorId.data,badActorType=form.badActorType.data,states=form.states.data, county=form.county.data,court=form.court.data)
        db.session.add(new_report)
        db.session.commit()
        return redirect(url_for('registry.entryViolations'))
    return render_template('registry/addgrievance.html', form=form)

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
