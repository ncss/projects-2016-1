import server.util as util
from db import User, Mist, ListContent

from templater import templater

def index_handler(response):
    if response.get_secure_cookie("user_id") is not None:
        response.redirect('/dashboard')
    else:
        response.write(templater.render("templates/index.html", page_title="Welcome to M'lists", site_title="M'lists"))
    
def post_login_handler(response):
    username = response.get_field("username", "")
    password = response.get_field("password", "")
    user = User.authenticate(username, password)
    if user:
        response.set_secure_cookie('user_id', '-1')
        response.redirect('/dashboard')
    else:
        response.redirect("/")

def get_login_handler(response):
    if response.get_secure_cookie('user_id') is not None:
        response.redirect('/dashboard')
    else:
        response.write(templater.render("templates/login_page.html", page_title="Login", site_title = "M'lists"))

def get_signup_handler(response):
    if response.get_secure_cookie('user_id') is not None:
        response.redirect('/dashboard')
    else:
        response.write(templater.render("templates/signup_page.html", page_title="Sign Up", site_title = "M'lists"))

def post_signup_handler(response):
    email = response.get_field("email", "")
    username = response.get_field("username", "")
    password = response.get_field("password", "")
    print("email: ", email, "username: ", username, "password: ", password)

    #TODO hit the database, create a new user, and set the cookie with the new user's id
    response.redirect("/")
    # give those things to the data base
    

# messing around with login handler clearing cookie and redirecting to a page
def logout_handler(response):
    response.clear_cookie('user_id')
    response.redirect('/')

@util.requires_login
def feed_handler(response):
    response.write(templater.render("templates/feed.html", page_title = "Feed", site_title = "M'lists"))

# dashboard integrates profile
@util.requires_login
def dashboard_handler(response):
        response.write(templater.render("templates/dashboard.html", page_title = "Dashboard", site_title = "M'lists"))


#@util.requires_login
def create_handler(response):
    response.write(templater.render("templates/create.html", page_title = "Create", site_title = "M'lists"))

#@util.requires_login
def create_post_handler(response):
	title = response.get_field("title", "")
	list_items = []
	index = 1
	while response.get_field("list_item_{}".format(index), "") != "":
		list_items.append(response.get_field("list_item_{}".format(index)))
		index += 1
    
	list = Mist(title, response.get_secure_cookie("user_id"))
	list.save()
	for i, item in enumerate(list_items):
		list_content = ListContent(list.id, i, item)
		list_content.save()
		
	print("Creating post: {}, {}".format(title, list_items))
	
	response.redirect('/dashboard')

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
                     
