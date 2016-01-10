import server.util as util
from db import User
from models.list_content import ListContent

from templater import templater

@util.requires_login
def index_handler(response):
    response.write("<h1>Hello, World! </h1> <p>user_id = {}</p>".format(response.get_secure_cookie('user_id')))
    #if cookie[user_id] != None:
        #username = database.get_username(cookie["user_id"])
        #response.write(render_template("index.html", username = username))
    #else:
        #response.write(render_template("index.html", username = None)                                  

def login_handler(response):
    username = response.get_field("username", "")
    password = response.get_field("password", "")
    User.authenticate(username, password)
    response.set_secure_cookie('user_id', '-1')
    response.write("<h1>Login Page</h1>")
    response.redirect('/')

# messing around with login handler clearing cookie and redirecting to a page
def logout_handler(response):
    response.clear_cookie('user_id')
    response.redirect('/')

def feed_handler(response):
    response.write("<h1> ( ͡° ͜ʖ ͡°) FEED ( ͡° ͜ʖ ͡°) </h1>")

# dashboard integrates profile
def dashboard_handler(response):
    response.write("<h1> ( ͡° ͜ʖ ͡°) DASHBOARD ( ͡° ͜ʖ ͡°) </h1>")

def create_handler(response):
    response.write("<h1> ( ͡° ͜ʖ ͡°) CREATE DEM MISTS ( ͡° ͜ʖ ͡°) </h1>")

def mini_list_handler(response):
    import sqlite3
    conn = sqlite3.connect("database.db")
    import os
    print("Debugging: ", os.getcwd())
##    conn.executescript(open('sql\init.sql').read())
    ListContent.connect(conn)
    mist = ListContent.findByListId(0)
    response.write(templater.render("mini_list.html", mist = mist))

# NEED MIST ID BEFORE THIS WILL WORK
#def view_handler(reponse):
    #response.write("<h1> ( ͡° ͜ʖ ͡°) VIEW DEM MISTS ( ͡° ͜ʖ ͡°) </h1>")
    
# NEED MIST ID BEFORE THIS WILL WORK
#def edit_handler(response):
    #response.write("<h1> ( ͡° ͜ʖ ͡°) EDIT DEM MISTS ( ͡° ͜ʖ ͡°) </h1>")

def settings_handler(response):
    response.write("<h1> ( ͡° ͜ʖ ͡°) CHANGE YA PROFILE SETTINGS ( ͡° ͜ʖ ͡°) </h1>")
                     
