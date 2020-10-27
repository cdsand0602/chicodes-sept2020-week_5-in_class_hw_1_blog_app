# Import the app variable from the init
from hw_1_blog_app import app

# Import specific packages from flask
from flask import render_template

# Default Home Route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/fav5')
def fav5Route():
    names = ['Prince','Michael Jackson','Madonna','Jamiroquai','Peven Everrett']
    return render_template('fav5.html',list_names = names)