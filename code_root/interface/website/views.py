from flask import Blueprint, render_template

#store a bunch of standard roots, where users can go to
#blueprint means a bunch of urls??? 

views = Blueprint('views', __name__)

@views.route('/')
def home(): #function will run whenver go to page
    return render_template("home.html")

@views.route('/schedule')
def schedule():
    return "<h1>Scheduling Logic</h1>"

@views.route('/data')
def data():
    return "<h1>Main data interface</h1>"

@views.route('/settings')
def settings():
    return "<h1>Settings Logic</h1>"