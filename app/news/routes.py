from flask import Flask, render_template, request, url_for, flash, redirect
from app.news import bp
from app.extensions import db
from app.models import Article
from datetime import datetime



@bp.route('/')
def index():
    news = Article.query.all()
    return render_template('news/index.html', news=news)


@bp.route('/categories/', methods=('GET', 'POST'))
def categories():

    if request.method == 'POST':
        new_question = Article(title=request.form['content'],
                               content=request.form['answer'])
        db.session.add(new_question)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('news/categories.html')

@bp.route('/addArticle/', methods=('GET', 'POST'))
def addArticle():

    if request.method == 'POST':
        new_article = Article(title=request.form['title'], author=request.form['author'],
            content=request.form['content'])
        db.session.add(new_article)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('news/addArticle.html')