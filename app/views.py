from flask import render_template
from app import app
from .request import businessArticles, entArticles, get_news_source, healthArticles, publishedArticles, randomArticles, scienceArticles, sportArticles, techArticles, topHeadlines
#views
@app.route('/')
def index():

    articles = publishedArticles()

    return  render_template('index.html', articles = articles)