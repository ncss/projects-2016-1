import sys

print(sys.version_info)

from tornado.ncss import Server

server = Server()

def index_handler(response):
    response.write("<h1>Hello, World! </h1>")


def meme_handler(response):
    response.write("m" + "e"*1337 + "mes")
# Handlers
server.register(r'/', index_handler)
server.register(r'/memes', meme_handler)


server.run()
