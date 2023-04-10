from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/posts')
def posts():
    return render_template('posts.html')

@app.route('/Cantonese')
def Cantonese():
    return render_template('cantonese_helper.html')

@app.route('/Vietnamese')
def Vietnamese():
    return render_template('vietnamese_helper.html')



