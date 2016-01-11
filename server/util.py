from templater import templater
from db import User


def requires_login(fn):
    def result(response):
        if response.get_secure_cookie('user_id') is not None:
            return fn(response)
        else:
            response.write(templater.render("templates/login_page.html"))
            username = response.get_field("username", "")
            password = response.get_field("password", "")
            user = User.authenticate(username, password)
            if user:
                response.set_secure_cookie('user_id', '-1')
                response.redirect('/dashboard')
    return result
