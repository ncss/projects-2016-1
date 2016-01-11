CREATE TABLE users (
  id    INTEGER PRIMARY KEY AUTOINCREMENT,
  username    TEXT    NOT NULL UNIQUE,
  password    TEXT    NOT NULL
);

CREATE TABLE lists (
  id	INTEGER	PRIMARY KEY	NOT NULL,
  name TEXT NOT NULL,
  author INT NOT NULL
);

CREATE TABLE list_contents (
  id INTEGER NOT NULL, 
  content    TEXT     NOT NULL,
  list    INT    NOT NULL,
  item_order  INT    NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (list) REFERENCES lists (id)
);

CREATE TABLE likes (
  person    INT    NOT NULL,
  list    INT    NOT NULL
);

CREATE TABLE imdb (
  id    INTEGER PRIMARY KEY    AUTOINCREMENT,
  imdb_id    TEXT    NOT NULL UNIQUE,
  title    TEXT    NOT NULL,
  year    TEXT,
  plot    TEXT,
  actors    TEXT,
  image    TEXT
);


