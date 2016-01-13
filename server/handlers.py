import sqlite3
import server.util as util
import json
import jinja2

from db import User
from models.list import List
from models.likes import Likes
from models.list_content import ListContent
from models.imdb import IMDB

from templater import templater

def index_handler(response):
    if util.is_logged_in(response):
        response.redirect('/dashboard')
    else:
        response.write(templater.render("templates/index.html", page_title="Welcome to M'lists", site_title="M'lists", response=response))

def post_login_handler(response):
    username = response.get_field("username", "")
    password = response.get_field("password", "")
    user = User.authenticate(username, password)
    if user:
        response.set_secure_cookie('user_id', str(user.id))
        response.redirect('/dashboard')

    else:
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

@util.requires_login
def logout_handler(response):
    response.clear_cookie('user_id')
    response.redirect('/')

@util.requires_login
def feed_handler(response):
    mists = List.find_all()

    popular = sorted(mists, key = lambda list: list.get_likes())
    popular.reverse()

    recent = sorted(mists, key = lambda list: list.id)
    recent.reverse()

    user_id = util.get_current_user_id(response)
    response.write(templater.render("templates/feed.html", mists=recent, popular=popular, page_title = "Feed", site_title = "M'lists", user_id=user_id))

# dashboard integrates profile
@util.requires_login
def dashboard_handler(response):
    uid = util.get_current_user_id(response)
    user_mists = List.find_by_userid(uid)
    recent = sorted(user_mists, key = lambda list: list.id)
    recent.reverse()
    user_id = util.get_current_user_id(response)
    response.write(templater.render("templates/dashboard.html", mists=recent, page_title = "Dashboard", site_title = "M'lists", user_id=user_id, image_fetcher=IMDB.fetch_image))

@util.requires_login
def create_handler(response):
    response.write(templater.render("templates/create.html", page_title = "Create", site_title = "M'lists", fail=response.get_field('fail', '')))

def privacy_handler(response):
    response.write(templater.render("templates/privacy.html", page_title = "Privacy", site_title = "M'lists"))

def terms_handler(response):
    response.write(templater.render("templates/terms.html", page_title = "Terms", site_title = "M'lists"))

@util.requires_login
def create_post_handler(response):
    title = response.get_field("title", "")
    if title.strip() == "":
        response.redirect("/create?fail=list_title_empty")
        return
    list_items = response.get_arguments("list_item")
    list_items = filter(None, list_items)
    a_list = List(title, util.get_current_user_id(response))
    a_list.save()
    for i, item in enumerate(list_items):
        list_content = ListContent.create(a_list.id, i, item)

    response.redirect('/dashboard')

# Make lists public to everyone
def view_handler(response, list_id):
    list = List.find(list_id)
    try:
        user_id = util.get_current_user_id(response)
    except Exception as e:
        user_id = None

    response.write(templater.render("templates/view_list.html", mist = list, page_title = list.name, site_title = "M'lists", user_id=user_id, image_fetcher=IMDB.fetch_image))

@util.requires_login
def edit_handler(response, list_id):
    user_id = util.get_current_user_id(response)
    list = List.find(list_id)

    if not list.author == user_id:
        raise Exception

    response.write(templater.render("templates/edit.html", mist = list, page_title = "Edit", site_title = "M'lists", fail=response.get_field('fail', '')))

@util.requires_login
def edit_post_handler(response, list_id):
    # Put this early otherwise all the items are removed!
    if response.get_field("title", "") == "":
        response.redirect("/list/{}/edit?fail=list_title_empty".format(list_id))
        return

    a_list = List.find(list_id)

    user_id = util.get_current_user_id(response)
    if not a_list.author == user_id:
        raise Exception

    a_list.name = response.get_field("title", "")
    a_list.save()

    # delete the old list items before adding the new ones
    for old_item in ListContent.find_by_list_id(list_id):
        ListContent.delete(list_id, old_item.item_order)

    list_items = response.get_arguments("list_item")
    list_items = filter(None, list_items)
    for i, item in enumerate(list_items):
        list_content = ListContent.create(a_list.id, i, item)

    response.redirect('/dashboard')

@util.requires_login
def delete_handler(response, list_id):
    a_list = List.find(list_id)

    user_id = util.get_current_user_id(response)
    if not a_list.author == user_id:
        raise Exception

    # delete the old list items before adding the new ones
    for old_item in ListContent.find_by_list_id(list_id):
        ListContent.delete(list_id, old_item.item_order)

    a_list.delete()
    response.redirect('/dashboard')

@util.requires_login
def post_like_handler(response):
    user_id = response.get_secure_cookie('user_id')
    list_id = response.get_field('list_id')

    l = Likes(user_id, list_id)
    l.create(user_id, list_id)

    likes = Likes.list_likes(list_id)

    response.set_header('Content-Type', 'application/json')
    response.write(json.dumps({'likes':likes}))

@util.requires_login
def post_unlike_handler(response):
    user_id = response.get_secure_cookie('user_id')
    list_id = response.get_field('list_id')

    l = Likes(user_id, list_id)
    l.remove(user_id, list_id)

    likes = Likes.list_likes(list_id)

    response.set_header('Content-Type', 'application/json')
    response.write(json.dumps({'likes':likes}))

def page_not_found_handler(response, path):
    response.set_status(404, 'Page not found')
    response.write(templater.render("templates/404.html", page_title="Page not found", site_title="M'lists"))

def meme_handler(response):
    response.redirect('http://blaker.space')
