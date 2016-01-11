from tornado.ncss import Server

import server.handlers as handlers
import templater
import db

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
server.register(r'/login', handlers.get_login_handler, post = handlers.post_login_handler)
server.register(r'/logout', handlers.logout_handler)
server.register(r'/signup', handlers.signup_handler)
server.register(r'/feed', handlers.feed_handler)
server.register(r'/dashboard', handlers.dashboard_handler)
server.register(r'/create', handlers.create_handler)
server.register(r'/create/post', handlers.create_post_handler)
#server.register(r'/{}/edit'.format(), handlers.edit_handler)
server.register(r'/settings', handlers.settings_handler)
#server.register(r'/mist', handlers.mini_list_handler)
#server.register(r'/dashboard/settings', handlers.settings_handler)
#server.register(r'/create/post', handlers.create_post_handler)
server.register(r'/view/(0-9)+', handlers.view_list_handler)
#server.register(r'/{}/edit'.format(), handlers.edit_handler)
server.register(r'/settings', handlers.settings_handler)
#server.register(r'/mist', handlers.mini_list_handler)
server.register(r'/like', post=handlers.post_like_handler)
server.register(r'/dashboard/settings', handlers.settings_handler)

server.run()
