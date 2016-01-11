DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id    INTEGER PRIMARY KEY AUTOINCREMENT,
  username    TEXT    NOT NULL UNIQUE,
  password    TEXT    NOT NULL
);
DROP TABLE IF EXISTS lists;
CREATE TABLE lists (
  id	INTEGER	PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  author INT NOT NULL, 
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
  user_id    INT    NOT NULL,
  list_id    INT    NOT NULL,
  UNIQUE(user_id, list_id) ON CONFLICT REPLACE,
  FOREIGN KEY(user_id) REFERENCES users(id),
  FOREIGN KEY(list_id) REFERENCES lists(id)
);

INSERT INTO lists VALUES (0, 'top ten movies1', 0);
INSERT INTO lists VALUES (1, 'top ten movies2', 1);
INSERT INTO lists VALUES (2, 'top ten movies3', 2);
INSERT INTO lists VALUES (3, 'top ten movies4', 3);
INSERT INTO lists VALUES (4, 'top ten movies5', 4);

INSERT INTO list_contents VALUES (5, 1, 'Hackers');
INSERT INTO list_contents VALUES (5, 3, 'Star Wars: the force awakens');
INSERT INTO list_contents VALUES (5, 2, 'Spectre James Bond');
INSERT INTO list_contents VALUES (5, 4, 'The Arrow');
INSERT INTO list_contents VALUES (5, 5, 'Pokemon Indigo league');

INSERT INTO likes VALUES (NULL, 0, 0);
INSERT INTO likes VALUES (NULL, 0, 1);
INSERT INTO likes VALUES (NULL, 1, 0);
INSERT INTO likes VALUES (NULL, 2, 2);
INSERT INTO likes VALUES (NULL, 2, 3);
INSERT INTO likes VALUES (NULL, 2, 4);
