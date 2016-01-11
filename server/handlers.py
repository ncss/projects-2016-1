import server.util as util
#from db import User
from templater import templater

@util.requires_login
def index_handler(response):
    response.write(templater.render("templates/index.html", page_title="Login", site_title="M'lists"))
    #if cookie[user_id] != None:
        #username = database.get_username(cookie["user_id"])
        #response.write(render_template("index.html", username = username))
    #else:
        #response.write(render_template("index.html", username = None)                                  

def post_login_handler(response):
    username = response.get_field("username", "")
    password = response.get_field("password", "")
    user = User.authenticate(username, password)
    if user:
        response.set_secure_cookie('user_id', '-1')
        response.redirect('/dashboard')

def get_login_handler(response):
    if response.get_secure_cookie('user_id'):
        response.redirect('/dashboard')
    else:
        response.write(templater.render("templates/login_page.html", page_title="Login", site_title = "M'lists"))


# messing around with login handler clearing cookie and redirecting to a page
def logout_handler(response):
    response.clear_cookie('user_id')
    response.redirect('/')

def feed_handler(response):
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
    response.write(templater.render("templates/feed.html", new_mists=new_mists, page_title = "Feed", site_title = "Mists"))
    
# dashboard integrates profile
def dashboard_handler(response):
    response.write(templater.render("templates/dashboard.html"))

def create_handler(response):
    response.write(templater.render("templates/create.html",page_title = "Create", site_title = "Mists"))
    #if get_secure_cookie:
        # send data to server
    #else:
        #response.write(templater.render("templates/login_page.html"))
    

#def edit_handler(response):
    # get list id
    # look up list
    # print list items in form sections
    # submit new list to DB

# NEED MIST ID BEFORE THIS WILL WORK
#def view_handler(reponse):
    #response.write("<h1> ( ͡° ͜ʖ ͡°) VIEW DEM MISTS ( ͡° ͜ʖ ͡°) </h1>")
    
# NEED MIST ID BEFORE THIS WILL WORK
#def edit_handler(response):
    #response.write("<h1> ( ͡° ͜ʖ ͡°) EDIT DEM MISTS ( ͡° ͜ʖ ͡°) </h1>")

def settings_handler(response):
    response.write("<h1> ( ͡° ͜ʖ ͡°) CHANGE YA PROFILE SETTINGS ( ͡° ͜ʖ ͡°) </h1>")
                     
