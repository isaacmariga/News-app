from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources, get_articles, get_highlights, get_categories



# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_categories = get_sources('general')
   
    entertainment_categories = get_sources('entertainment')
    sports_categories = get_sources('sports')
    technology_categories = get_sources('technology')
    science_category = get_sources('science')
    health_category = get_sources('health')


    title = 'Todays News'

    return render_template('index.html',title = title, general = general_categories, business = entertainment_categories)

@main.route('/newsarticle/<id>')
def newsarticle(id):

    '''
    View article page function that returns the article details page and its data
    '''
    articles_items = get_articles(id)
    title = f'{id} | News Articles'
    return render_template('articles.html',title = title, articles = articles_items)

@main.route('/category/<category>')
def category(category):

    '''
    View article page function that returns the article details page and its data
    '''
    category_items = get_categories(category)
    title = f'{category} | News Articles'
    return render_template('categories.html',title = title, items = category_items)


@main.route('/*')
def error():
  
    return render_template('error.html')
