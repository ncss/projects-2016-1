import server.util as util
from db import User

from models.list_content import ListContent

from templater import templater

def index_handler(response):
    if response.get_secure_cookie("user_id") is not None:
        response.redirect('/dashboard')
    else:
        response.write(templater.render("templates/index.html", page_title="Login", site_title="M'lists"))

def post_login_handler(response):
    print("Mems")
    username = response.get_field("username", "")
    password = response.get_field("password", "")
    user = User.authenticate(username, password)
    if user:
        response.set_secure_cookie('user_id', '-1')
        response.redirect('/dashboard')

    response.write(templater.render("templates/login_page.html", page_title="Login", site_title = "M'lists"))

def get_login_handler(response):
    if response.get_secure_cookie('user_id') is not None:
        response.redirect('/dashboard')
    else:
        response.write(templater.render("templates/login_page.html", page_title="Login", site_title = "M'lists"))

def signup_handler(response):
    response.write(templater.render("templates/signup_page.html", page_title="Sign Up", site_title = "M'lists"))

# messing around with login handler clearing cookie and redirecting to a page
def logout_handler(response):
    response.clear_cookie('user_id')
    response.redirect('/')

@util.requires_login
def feed_handler(response):
    response.write(templater.render("templates/feed.html", page_title = "Feed", site_title = "Mists"))

# dashboard integrates profile
@util.requires_login
def dashboard_handler(response):
    new_mists = [
        {
            "title": "Top 10 Action Movies",
            "content": ["James Bond", "The Matrix", "Taken", "The Dark Night", "Star Wars", "The Avengers", "Mad Max", "Aliens", "The Terminator", "Rambo"]
        },
        {
            "title": "Top 10 Adventure Movies",
            "content": ["James Bond", "The Matrix", "Taken", "The Dark Night", "Star Wars", "The Avengers", "Mad Max", "Aliens", "The Terminator", "Rambo"]
        }
    ]
    response.write(templater.render("templates/dashboard.html",mists=new_mists, page_title = "Dashboard", site_title = "Mists"))

@util.requires_login
def create_handler(response):
    response.write(templater.render("templates/create.html", page_title = "Create", site_title = "Mists"))

@util.requires_login
def create_post_handler(response):
    print(response.get_field("title"))

def mini_list_handler(response):
    import sqlite3
    conn = sqlite3.connect("database.db")
    import os
    print("Debugging: ", os.getcwd())
##    conn.executescript(open('sql\init.sql').read())
    ListContent.connect(conn)
    mist = ListContent.findByListId(0)
    response.write(templater.render("mini_list.html", mist = mist))

def view_list_handler(response, list_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM likes WHERE list_id=?;", (list_id))
    likes = c.fetchone()

    list = {
            "title": "Top 10 Adventure Movies",
            "description": "A list about adventure movies",
            "content": ["James Bond", "The Matrix", "Taken", "The Dark Night", "Star Wars", "The Avengers", "Mad Max", "Aliens", "The Terminator", "Rambo"]
        }

    response.write(templater.render('templates/view_list.html', likes=likes, list=list))

# NEED MIST ID BEFORE THIS WILL WORK
#def edit_handler(response):
    #response.write("<h1> ( ͡° ͜ʖ ͡°) EDIT DEM MISTS ( ͡° ͜ʖ ͡°) </h1>")

def settings_handler(response):
    response.write("<h1> ( ͡° ͜ʖ ͡°) CHANGE YA PROFILE SETTINGS ( ͡° ͜ʖ ͡°) </h1>")

def post_like_handler(response):
    user_id = response.get_field('user_id')
    list_id = response.get_field('list_id')

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM likes WHERE user_id=?, list_id=?;", (user_id, list_id))
    if c.fetchone() == 0:
        c.execute('INSERT INTO likes VALUES(NULL, ?,?);', (user_id, list_id))
        conn.commit()

    conn.close()

    response.write('')
