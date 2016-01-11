import requests


class IMDB:
  baseURL = "http://www.omdbapi.com"

  def __init__(self,imdb_id,title,year,plot,actors,image,id=None):
    self.id = id
    self.imdb_id = imdb_id
    self.title = title
    self.year = year
    self.plot = plot
    self.actors = actors
    self.image = image

  def get_trailer(self):
    return "http://www.imdb.com/title/{}/trailers".format(self.imdb_id)
  
  @classmethod
  def connect(cls, conn):
    cls.conn = conn

  @classmethod
  def fetch_api_id(cls, id):
    r = requests.get('{}/?i={}&plot=short&r=json'.format(cls.baseURL,id))
    return cls._to_obj(r)

  @classmethod
  def fetch_api_name(cls, name):
    r = requests.get('{}/?t={}&plot=short&r=json'.format(cls.baseURL,name))
    return cls._to_obj(r)

  @classmethod
  def _to_obj(cls, r):
    # Check if the api errors
    print(r.text)
    res = r.json()

    if res["Response"] == "False":
      return None
    return cls(
      imdb_id=res["imdbID"],
      title=res["Title"],
      year=res["Year"],
      plot=res["Plot"],
      actors=res["Actors"],
      image=res["Poster"]
    )
  
  @classmethod
  def fetch_image(cls,name):
    obj = cls.fetch_api_name(name)
    if obj is None:
      return "placeholder.png"
    return obj.image

  @classmethod
  def fetch_thumbnail(cls,name):
    obj = cls.fetch_api_name(name)
    if obj is None:
      return "placeholder.png"
    return obj.image
