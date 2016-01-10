from tornado.ncss import Server

'''
TO DO LIST:
- add list_id to the URL for registering view and edit
- complete handler functions for:
    - feed_handler
    - dashboard_handler
    - create_handler
    - view_handler
    - edit_handler
    - settings_handler
'''


server = Server()

def index_handler(response):
    response.write("<h1>Hello, World! </h1> <p>user_id = {}</p>".format(response.get_secure_cookie('user_id')))
    #if cookie[user_id] != None:
        #username = database.get_username(cookie["user_id"])
        #response.write(render_template("index.html", username = username))
    #else:
        #response.write(render_template("index.html", username = None)                                  

def login_handler(response):
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

# NEED MIST ID BEFORE THIS WILL WORK
#def view_handler(reponse):
    #response.write("<h1> ( ͡° ͜ʖ ͡°) VIEW DEM MISTS ( ͡° ͜ʖ ͡°) </h1>")
    
# NEED MIST ID BEFORE THIS WILL WORK
#def edit_handler(response):
    #response.write("<h1> ( ͡° ͜ʖ ͡°) EDIT DEM MISTS ( ͡° ͜ʖ ͡°) </h1>")

def settings_handler(response):
    response.write("<h1> ( ͡° ͜ʖ ͡°) CHANGE YA PROFILE SETTINGS ( ͡° ͜ʖ ͡°) </h1>")
                     

# Handlers
server.register(r'/', index_handler)
server.register(r'/login', login_handler)
server.register(r'/logout', logout_handler)
server.register(r'/feed', feed_handler)
server.register(r'/dashboard', dashboard_handler)
server.register(r'/create', create_handler)
#server.register(r'/{}/view'.format(), view_handler)
#server.register(r'/{}/edit'.format(), edit_handler)
server.register(r'/settings', settings_handler)

server.run()
