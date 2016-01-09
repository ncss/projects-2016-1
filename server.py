from tornado.ncss import Server

server = Server()

# Handlers
server.register(r'/',index_handler)


server.run()
