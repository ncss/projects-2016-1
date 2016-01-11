from templater import templater

from  models import User



def requires_login(fn):
    def result(response, *args, **kwargs):
        if response.get_secure_cookie('user_id') is not None:
            return fn(response, *args, **kwargs)
        else:
            response.write(templater.render("templates/login_page.html", page_title="Login", site_title="M'lists",login_failed=False))
    return result

def get_current_user_id(response):
    uid = response.get_secure_cookie("user_id")
    if uid is None:
        raise Exception("No user is currently logged in")
    return uid

def is_logged_in(response):
    return response.get_secure_cookie("user_id") is not None
