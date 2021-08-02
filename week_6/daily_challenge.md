-- daily_challenge

CREATE TABLE actors(
 id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age smallint NOT NULL,
 number_oscars SMALLINT NOT NULL
);


select count(id) from actors;
-- select count(id) from actors;
insert into actors(first_name, last_name, age, number_oscars)
VALUES('Anglelina','July',null, 3);
-- can't add null because of not null.

