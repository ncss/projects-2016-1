from tornado.ncss import Server

server = Server()

def index_handler(response):
  response.write("Hello World")

# Handlers
server.register(r'/',index_handler)


server.run()
