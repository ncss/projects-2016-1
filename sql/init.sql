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
  FOREIGN KEY(user_id) REFERENCES users(id),
  FOREIGN KEY(list_id) REFERENCES lists(id)
);

INSERT INTO users VALUES (NULL, 'cool_hax1', 'coolhax1');
INSERT INTO users VALUES (NULL, 'cool_hax2', 'coolhax2');
INSERT INTO users VALUES (NULL, 'cool_hax3', 'coolhax3');
INSERT INTO users VALUES (NULL, 'cool_hax4', 'coolhax4');
INSERT INTO users VALUES (NULL, 'cool_hax5', 'coolhax5');

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

INSERT INTO likes VALUES (NULL, 0, 0);
INSERT INTO likes VALUES (NULL, 0, 1);
INSERT INTO likes VALUES (NULL, 1, 0);
INSERT INTO likes VALUES (NULL, 2, 2);
INSERT INTO likes VALUES (NULL, 2, 3);
INSERT INTO likes VALUES (NULL, 2, 4);
