CREATE TABLE people (
  id INTEGER NOT NULL,
  fname TEXT NOT NULL,
  lname TEXT NOT NULL,
  gender TEXT NOT NULL,
  age INTEGER NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE events (
  id INTEGER NOT NULL,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  gender TEXT NOT NULL,
  at TEXT NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE results (
  event INTEGER NOT NULL,
  person INTEGER NOT NULL,
  result TEXT,
  PRIMARY KEY (event, person),
  FOREIGN KEY (event) REFERENCES events (id),
  FOREIGN KEY (person) REFERENCES people (id)
);

INSERT INTO people VALUES (      0, 'Barry', 'Schultz', 'M', 16);
INSERT INTO people VALUES (      1, 'Prue', 'Robinson', 'F', 17 );
INSERT INTO people VALUES (      2, 'Andrew', 'Varvel', 'M', 16 );
INSERT INTO people VALUES (      3, 'Mathew', 'Nemes', 'M', 13 );
INSERT INTO people VALUES (      4, 'Mara', 'Barber', 'F', 17 );
INSERT INTO people VALUES (      5, 'Scott', 'Herdman', 'M', 16 );
INSERT INTO people VALUES (      6, 'Alec', 'Newton', 'M', 16 );
INSERT INTO people VALUES (      7, 'Karen', 'Barber', 'F', 14 );
INSERT INTO people VALUES (      8, 'Grant', 'Ovzinsky', 'M', 17 );

INSERT INTO events VALUES (      0, '100m', 16, 'M', '09:10' );
INSERT INTO events VALUES (      1, '200m', 16, 'M', '09:15' );
INSERT INTO events VALUES (      2, '100m', 17, 'M', '09:00' );
INSERT INTO events VALUES (      3, '100m', 17, 'F', '09:05' );

INSERT INTO results VALUES (      0, 5, '00:21');
INSERT INTO results VALUES (      0, 0, '00:15');
INSERT INTO results VALUES (      3, 1, '00:20');
INSERT INTO results VALUES (      0, 2, '00:17');
INSERT INTO results VALUES (      0, 6, NULL);
INSERT INTO results VALUES (      3, 4, '00:20');
INSERT INTO results VALUES (      2, 8, NULL);
INSERT INTO results VALUES (      1, 0, '00:40');
