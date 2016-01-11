import sqlite3
import server.util as util
import json
from db import User
from models.list import List
from models.likes import Likes
from models.list_content import ListContent
import sqlite3
from models.imdb import IMDB

from templater import templater

def index_handler(response):
    print(response.get_secure_cookie("user_id"))
    if is_logged_in(response):
        response.redirect('/dashboard')
    else:
        response.write(templater.render("templates/index.html", page_title="Welcome to M'lists", site_title="M'lists", response=response))

def post_login_handler(response):
    username = response.get_field("username", "")
    password = response.get_field("password", "")
    user = User.authenticate(username, password)
    if user:
        response.set_secure_cookie('user_id', str(user.id))
        print("Authenticated user %s" % user.id)
        response.redirect('/dashboard')

    else:
        print("Not logged in")
        response.redirect("/login?fail=1")

def get_login_handler(response):
    if response.get_secure_cookie('user_id') is not None:
        response.redirect('/dashboard')
    else:
        login_failed = response.get_field('fail', '') == '1'
        response.write(templater.render("templates/login_page.html", login_failed=login_failed,
                                        page_title="Login", site_title="M'lists"))

def post_signup_handler(response):
    email = response.get_field("email", "")
    username = response.get_field("username", "")
    password = response.get_field("password", "")

    if username == "" or password == "":
        response.redirect("/signup")
        return

    user = User(username, password)

    try:
        user.save()
    except sqlite3.IntegrityError:
        response.redirect("/signup?fail=user_exists")
    else:
        response.set_secure_cookie("user_id", str(user.id))
        response.redirect("/")

def logout_handler(response):
    response.clear_cookie('user_id')
    response.redirect('/')

@util.requires_login
def feed_handler(response):
    mists = List.find_all()
    popular = sorted(mists, key = lambda list: list.get_likes())
    popular.reverse()
	
    user_id = get_current_user_id(response)
    response.write(templater.render("templates/feed.html", mists=mists, popular=popular, page_title = "Feed", site_title = "M'lists", user_id=user_id))

# dashboard integrates profile
@util.requires_login
def dashboard_handler(response):
    uid = get_current_user_id(response)
    user_mists = List.find_by_userid(uid)
    user_id = get_current_user_id(response)
    response.write(templater.render("templates/dashboard.html", mists=user_mists, page_title = "Dashboard", site_title = "M'lists", user_id=user_id, image_fetcher=IMDB.fetch_image))

@util.requires_login
def create_handler(response):
    response.write(templater.render("templates/create.html", page_title = "Create", site_title = "M'lists"))

def privacy_handler(response):
    response.write(templater.render("templates/privacy.html", page_title = "Privacy", site_title = "M'lists"))

def terms_handler(response):
    response.write(templater.render("templates/terms.html", page_title = "Terms", site_title = "M'lists"))

@util.requires_login
def create_post_handler(response):
    title = response.get_field("title", "")
    list_items = response.get_arguments("list_item")
    list_items = filter(None, list_items)
    a_list = List(title, get_current_user_id(response))
    a_list.save()
    for i, item in enumerate(list_items):
        list_content = ListContent.create(a_list.id, i, item)

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

# Make lists public to everyone
def view_handler(response, list_id):
    list = List.find(list_id)
    try:
        user_id = get_current_user_id(response)
    except Exception as e:
        user_id = None

    response.write(templater.render("templates/view_list.html", mist = list, page_title = list.name, site_title = "M'lists", user_id=user_id, image_fetcher=IMDB.fetch_image))

def edit_handler(response, list_id):
    list = List.find(list_id)
    response.write(templater.render("templates/edit.html", mist = list, page_title = "Edit", site_title = "M'lists"))

def edit_post_handler(response, list_id):
    a_list = List.find(list_id)

    for item in a_list.list_contents():
        item.remove()

    a_list.name = response.get_field("title", "")
    list_items = []
    index = 1
    while response.get_field("list_item_{}".format(index), "") != "":
        list_items.append(response.get_field("list_item_{}".format(index)))
        index += 1

    a_list.save()
    for i, item in enumerate(list_items):
        list_content = ListContent.create(a_list.id, i, item)

    print("Editing post: {}, {}".format(a_list.name, list_items))
    response.redirect('/dashboard')

def view_list_handler(response, list_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM likes WHERE list_id=?;", (list_id))
    likes = c.fetchone()

    list = {
            "title": "Top 10 Adventure Movies",
            "description": "A list about adventure movies",
            "content": ["James Bond", "The Matrix", "Taken", "The Dark Night", "Star Wars", "The Avengers", "Mad Max", "Aliens", "The Terminator", "Rambo"]
        }

    response.write(templater.render('templates/view_list.html', likes=likes, list=list))

def settings_handler(response):
    response.write("<h1> ( ͡° ͜ʖ ͡°) CHANGE YA PROFILE SETTINGS ( ͡° ͜ʖ ͡°) </h1>")

@util.requires_login
def post_like_handler(response):
    user_id = response.get_field('user_id')
    list_id = response.get_field('list_id')

    l = Likes(user_id, list_id)
    l.create(user_id, list_id)

    likes = Likes.list_likes(list_id)

    response.set_header('Content-Type', 'application/json')
    response.write(json.dumps({'likes':likes}))

@util.requires_login
def post_unlike_handler(response):
    user_id = response.get_field('user_id')
    list_id = response.get_field('list_id')

    l = Likes(user_id, list_id)
    l.remove(user_id, list_id)

    likes = Likes.list_likes(list_id)

    response.set_header('Content-Type', 'application/json')
    response.write(json.dumps({'likes':likes}))

def get_current_user_id(response):
    uid = response.get_secure_cookie("user_id")
    if uid is None:
        raise Exception("No user is currently logged in")
    return uid

def is_logged_in(response):
    return response.get_secure_cookie("user_id") is not None

def page_not_found_handler(response, path):
    #insert a html page for 404
    response.set_status(404, 'Page not found')
    response.write(templater.render("templates/404.html", page_title="Page not found", site_title="M'lists"))

def meme_handler(response):
    response.redirect('http://blaker.space')
