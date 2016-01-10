from tornado.ncss import Server

server = Server()

def index_handler(response):
    response.write("<h1>Hello, World! </h1> <p>user_id = {}</p>".format(response.get_secure_cookie('user_id')))
    


def login_handler(response):
    response.set_secure_cookie('user_id', '-1')
    response.write("<h1>Login Page</h1>")
    response.redirect('/')

# messing around with login handler clearing cookie and redirecting to a page
def logout_handler(response):
    response.clear_cookie('user_id')
    response.redirect('/')
    
# Handlers
server.register(r'/', index_handler)
server.register(r'/login', login_handler)
server.register(r'/logout', logout_handler)

server.run()
