from flask import Flask,jsonify,render_template, request, url_for, flash, redirect
from werkzeug.utils import secure_filename
import csv
import os
from app.api import bp
from app.extensions import db
from app.models import Actors, ActorType, Violations, Article, VioCategory, Orgs, States, Counties
from app.api.forms import AddTable
import simplejson as json
from app.models import actors_schema
from sqlalchemy import or_
from sqlalchemy.sql.operators import ilike_op,like_op

@bp.route('/returnnews', methods = ['GET']) 
def ReturnNews(): 
    if(request.method == 'GET'): 
        news = Article.query.all()
        print(news)
        return json.dumps([(dict(row.Article) for row in news)])

@bp.route('/allactors', methods = ['GET'])
def allActors():
    if(request.method == 'GET'):
        actors = Actors.query.all()
        return actors_schema.dump(actors)

@bp.route('/searchactors/<search_val>', methods = ['GET'])
def searchActors(search_val):
    val =search_val
    if(request.method == 'GET'):
        actors = Actors.query.filter(or_(ilike_op(Actors.lName,f'%{val}%'),ilike_op(Actors.fName,f'%{val}%') )).order_by(Actors.lName.desc())
        return actors_schema.dump(actors)

@bp.route('/uploadcsv', methods=('GET','POST'))
def uploadCSV():
    form = AddTable()
    if form.validate_on_submit():
        file = form.csvFile.data
        filename = secure_filename(file.filename)
        file.save('uploads/' + filename)
        with open('uploads/' + filename, newline = "", encoding = 'utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter = ',')
            tableType = form.tableType.data
            if tableType == 'actor_type':
                for row in csv_reader:
                    entry = ActorType(actorType=row[1])
                    db.session.add(entry)
                    db.session.commit()
            elif tableType == 'actors':
                for row in csv_reader:
                    entry = Actors(fName=row[1], lName=row[2])
                    db.session.add(entry)
                    db.session.commit()
            elif tableType == 'counties':
                for row in csv_reader:
                    entry = Counties(county=row[1], state=row[2])
                    db.session.add(entry)
                    db.session.commit()
            elif tableType == 'orgs':
                for row in csv_reader:
                    entry = Orgs(name=row[1], address1=row[2], address2=row[3], city=row[4], state=row[5],zipcode=row[6], phone=row[7], orgEmail=row[8], website=row[9])
                    db.session.add(entry)
                    db.session.commit()
            elif tableType == 'states':
                for row in csv_reader:
                    entry = States(abbrv=row[1], name=row[2])
                    db.session.add(entry)
                    db.session.commit()
            elif tableType == 'vio_category':
                for row in csv_reader:
                    entry = VioCategory(category=row[1])
                    db.session.add(entry)
                    db.session.commit()
            elif tableType == 'violations':
                for row in csv_reader:
                    entry = Violations(violation=row[1], violationTypeId=row[2])
                    db.session.add(entry)
                    db.session.commit()
            else:
                "table type not found"

        return redirect(url_for('main.index'))
    return render_template('api/uploadcsv.html', form=form)