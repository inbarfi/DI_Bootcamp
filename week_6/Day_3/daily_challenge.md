# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 13:47:56 2021

@author: Inbar
"""

#daily_challenge
-- CREATE TABLE people (
--   id SERIAL,
--   first_name VARCHAR(45) NOT NULL,
--   last_name VARCHAR(45) NOT NULL,
--   age SMALLINT NOT NULL,
--   PRIMARY KEY (id)
-- );

-- insert into people (first_name, last_name, age) values 
-- ('Ronny', 'Cohen', 35), ('Danny', 'Mizrachi', 45), 
-- ('Danny', 'Perelman', 55), ('Dafna', 'Amit', 66), 
-- ('Tom', 'Ziv', 22);

-- CREATE TABLE vaccinated (
-- 	people_id SERIAL,
-- 	vaccine_number SMALLINT NOT NULL,
-- 	FOREIGN KEY (people_id) REFERENCES people (id)	
-- );

-- Insert into vaccinated (vaccine_number) values 
-- (1 ,1), (2, 2), (3, 0), (4, 2), (5, 1); 

CREATE TABLE covid19(
	people_id SERIAL,
	positive SMALLINT NOT NULL,
	FOREIGN KEY (pepole_id) REFERENCES people (id)
);

-- INSERT INTO covid19(people_id, positive) VALUES 
-- (1, 1), (2, 0), (3, 1), (4, 0), (5, 0);

-- select * from people p
-- join vaccinated v
-- on p.id = v.people_id
-- join covid19 c
-- on c.people_id = p.id;

-- select * from people p
-- INNER JOIN vaccinated v
-- on p.id = v.people_id;

