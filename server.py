#!/usr/bin/env python3

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
'''

db.connect_or_create()
server = Server()

# Handlers
server.register(r'/', handlers.index_handler)
server.register(r'/login', handlers.get_login_handler, get = handlers.get_login_handler, post = handlers.post_login_handler)
server.register(r'/logout', handlers.logout_handler)
server.register(r'/signup', handlers.index_handler, post = handlers.post_signup_handler)
server.register(r'/feed', handlers.feed_handler)
server.register(r'/dashboard', handlers.dashboard_handler)
server.register(r'/create', handlers.create_handler, post = handlers.create_post_handler)
server.register(r'/list/(\d+)/view', handlers.view_handler)
server.register(r'/list/(\d+)/edit', handlers.edit_handler, post = handlers.edit_post_handler)
server.register(r'/list/(\d+)/delete', handlers.delete_handler)
server.register(r'/memes', handlers.meme_handler)
server.register(r'/privacy', handlers.privacy_handler)
server.register(r'/terms', handlers.terms_handler)
server.register(r'/like', handlers.post_like_handler)
server.register(r'/unlike', handlers.post_unlike_handler)

server.register(r'/(.*)', handlers.page_not_found_handler)

server.run()
