from flask import render_template
from app import app

#views
@app.route('/')
def index():

    articles = publishedArticles()

    return  render_template('index.html', articles = articles)