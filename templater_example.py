import templater

class User:
    def __init__(self, name):
        self.name = name

user = User("Tim Dawborn")
print(templater.render('docs/templater.md', user=user,
                       movie_list=["Aladdin", "Finding Nemo"],
                       var_name="Example variable",
                       page_title="Movie list",
                       site_title="List thing site",
                       expression=True))
