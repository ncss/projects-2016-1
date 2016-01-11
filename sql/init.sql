DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id    INTEGER PRIMARY KEY AUTOINCREMENT,
  username    TEXT    NOT NULL UNIQUE,
  password    TEXT    NOT NULL
);
DROP TABLE IF EXISTS lists;
CREATE TABLE lists (
  id	INTEGER	AUTOINCREMENT,
  name TEXT NOT NULL,
  author INT NOT NULL, 
  PRIMARY KEY (id), 
  FOREIGN KEY (author) REFERENCES users (id)
);
DROP TABLE IF EXISTS list_contents;
CREATE TABLE list_contents (
  list    INT    NOT NULL,
  item_order  INT    NOT NULL,
  content    TEXT     NOT NULL,
  PRIMARY KEY (list, item_order),
  FOREIGN KEY (list) REFERENCES lists (id)
);
DROP TABLE IF EXISTS likes;
CREATE TABLE likes (
  id    INTEGER PRIMARY KEY AUTOINCREMENT,
  person    INT    NOT NULL,
  list    INT    NOT NULL
  FOREIGN KEY (person) REFERENCES users(id),
  FOREIGN KEY (list) REFERENCES lists(id)
);
