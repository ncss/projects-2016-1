from templater import templater

from models import User

def requires_login(fn):
    def result(response):
        if response.get_secure_cookie('user_id') is not None:
            return fn(response)
        else:
            response.write(templater.render("templates/login_page.html", page_title="Login", site_title="M'lists",login_failed=False))
    return result
