DROP TABLE IF EXISTS USERS;
CREATE TABLE USERS
(
    Id SERIAL PRIMARY KEY,
    Email TEXT,
    FirstName TEXT,
    LastName TEXT
);
