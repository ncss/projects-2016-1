CREATE TABLE users (
  id    INTEGER PRIMARY KEY AUTOINCREMENT,
  username    TEXT    NOT NULL UNIQUE,
  password    TEXT    NOT NULL,
  name    TEXT    NOT NULL,
  email   TEXT    NOT NULL UNIQUE
);

CREATE TABLE lists (
  id	INTEGER	PRIMARY KEY	NOT NULL,
  name TEXT NOT NULL,
  author INT NOT NULL
);

CREATE TABLE list_contents (
  content    TEXT     NOT NULL,
  list    INT    NOT NULL
);

CREATE TABLE likes (
  person    INT    NOT NULL,
  list    INT    NOT NULL
);


