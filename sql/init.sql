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

INSERT INTO users VALUES (0, 'cool_hax1', 'coolhax1');
INSERT INTO users VALUES (1, 'cool_hax2', 'coolhax2');
INSERT INTO users VALUES (2, 'cool_hax3', 'coolhax3');
INSERT INTO users VALUES (3, 'cool_hax4', 'coolhax4');
INSERT INTO users VALUES (4, 'cool_hax5', 'coolhax5');

INSERT INTO lists VALUES (0, 'top ten movies1', 'john smith1');
INSERT INTO lists VALUES (1, 'top ten movies2', 'john smith2');
INSERT INTO lists VALUES (2, 'top ten movies3', 'john smith3');
INSERT INTO lists VALUES (3, 'top ten movies4', 'john smith4');
INSERT INTO lists VALUES (4, 'top ten movies5', 'john smith5');

/*
INSERT INTO list_contents VALUES (

INSERT INTO likes VALUES (
*/ 