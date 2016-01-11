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
  list    INT    NOT NULL,
  item_order  INT    NOT NULL,
  content    TEXT     NOT NULL,
  PRIMARY KEY (list, item_order),
  FOREIGN KEY (list) REFERENCES lists (id)
);

CREATE TABLE likes (
  id    INTEGER PRIMARY KEY AUTOINCREMENT,
  person    INT    NOT NULL,
  list    INT    NOT NULL
);

INSERT INTO lists VALUES (0, 'top ten movies1', 0);
INSERT INTO lists VALUES (1, 'top ten movies2', 1);
INSERT INTO lists VALUES (2, 'top ten movies3', 2);
INSERT INTO lists VALUES (3, 'top ten movies4', 3);
INSERT INTO lists VALUES (4, 'top ten movies5', 4);


INSERT INTO list_contents VALUES (0, 1, 'Hackers: this movie is really cool');
INSERT INTO list_contents VALUES (0, 3, 'Star Wars: this movie is really cool');
INSERT INTO list_contents VALUES (0, 2, 'Specter: this movie is really cool');
INSERT INTO list_contents VALUES (1, 2, 'The Arrow: this show is awesome');
INSERT INTO list_contents VALUES (2, 1, 'Pokemon Indigo league: this show is awesome');

/*
HOW DO YOU INSERT A VALUE INTO AN AUTOINCREMENT FIELD?
(THE FIRST COLUMN BELOW)
*/ 
INSERT INTO likes VALUES (0, 0, 0);
INSERT INTO likes VALUES (1, 0, 1);
INSERT INTO likes VALUES (2, 1, 0);
INSERT INTO likes VALUES (3, 2, 2);
INSERT INTO likes VALUES (4, 2, 3);
INSERT INTO likes VALUES (5, 2, 4);

INSERT INTO users VALUES (0, 'test', 'test');
