/*

______________USE THIS SCHEMA LATER, FOR NOW WE WILL USE INIT.sql AS A SAMPLE DATABASE

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

*/ 