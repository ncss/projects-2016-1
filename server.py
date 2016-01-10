from tornado.ncss import Server

import server.handlers as handlers

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


# Handlers
server.register(r'/', handlers.index_handler)
server.register(r'/login', handlers.login_handler)
server.register(r'/logout', handlers.logout_handler)
server.register(r'/feed', handlers.feed_handler)
server.register(r'/dashboard', handlers.dashboard_handler)
server.register(r'/create', handlers.create_handler)
#server.register(r'/{}/view'.format(), handlers.view_handler)
#server.register(r'/{}/edit'.format(), handlers.edit_handler)
server.register(r'/settings', handlers.settings_handler)

server.run()
