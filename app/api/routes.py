from flask import Flask,jsonify,render_template, request, url_for, flash, redirect
from app.api import bp
from app.extensions import db
from app.models import Actors, Article, States
from datetime import datetime
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
    print(val)
    if(request.method == 'GET'):
        actors = Actors.query.filter(or_(ilike_op(Actors.lName,f'%{val}%'),ilike_op(Actors.fName,f'%{val}%') )).order_by(Actors.lName.desc())
        return actors_schema.dump(actors)