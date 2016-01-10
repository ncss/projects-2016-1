

def requires_login(fn):
    def result(response):
        if response.get_secure_cookie('user_id') is not None:
            return fn(response)
        else:
            response.write("<p>Please log in.</p>")
    return result
