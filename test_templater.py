from templater import templater

print(templater.render("templater/test.html", page_title="page_title", xss_prevented="<h1>XSS Prevented!</h1>"))
