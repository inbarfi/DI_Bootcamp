"""
Created on Tue Aug  3 15:15:14 2021

@author: Inbar
"""

#xp
#1.1
-- select name from language;

#1.2
select title as film_name, name as language from film
left outer join language
on film.language_id = language.language_id;

select title as film_name, name from film
right outer join language
on film.language_id = language.language_id
where name != 'English'; -- null as all movies are in English

#1.3
-- CREATE TABLE new_film (
-- 	id SERIAL, 
-- 	name VARCHAR (50),
-- 	PRIMARY KEY (id)
-- );
--  INSERT INTO new_film(name) values ('Avengers3'), ('Sinderella'), ('Pokemon10');

#1.4
CREATE TABLE customer_review (
	review_id SERIAL NOT NULL, 
	film_id SERIAL,
	language_id SERIAL,
	title VARCHAR (50),
	score SMALLINT,
	review_text TEXT,
	last_update DATE,
	PRIMARY KEY (review_id),
	FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
	FOREIGN KEY (language_id) REFERENCES language (language_id)
);

#1.5
INSERT INTO customer_review(film_id, language_id, title, score, review_text, last_update)
VALUES 
(1, 1, 1, 'NY Times', 5, 'Excellent Movie!', '2019-09-28'), 
(2, 2, 1, 'The Guardian', 4, 'Brilliant.', '2020-01-12');

#1.6 - based on 1.5

#2.1
-- UPDATE film
-- SET language_id = 2
-- WHERE
--     film_id = 133;

select * from film
where film_id = 133;

#2.2
film_id & language_id - refering them on where clause like in 2.1

#2.3 
no

#2.4
SELECT * FROM public.rental
where return_date is null;

#2.5 - based on 2.4 
SELECT rental_id, return_date, amount
FROM public.rental r
JOIN payment p
on r.rental_id = p.rental_id
where return_date is null -- doesnt work (based on 2.4)
order by amount DESC
limit 30;

#2.6.1
SELECT f.title, f.film_id
FROM actor a
JOIN film_actor 
ON a.actor_id = film_actor.actor_id
JOIN film f
ON f.film_id = film_actor.film_id
WHERE first_name = 'Penelope' and last_name = 'Monroe' and f.description like '%Sumo%';

#2.6.2
SELECT f.title, f.film_id, f.rating, f.length, c.name
FROM film f
JOIN film_category
ON f.film_id = film_category.film_id
JOIN category c
ON c.category_id = film_category.category_id
WHERE f.length < 90 and f.rating = 'R' and c.name = 'Documentary'

#2.6.3
SELECT f.title, f.film_id
FROM customer c
JOIN payment p
ON c.customer_id = p.customer_id
JOIN rental r
ON r.rental_id = p.rental_id
JOIN inventory i
ON i.inventory_id = r.inventory_id
JOIN film f
ON f.film_id = i.film_id
WHERE c.first_name = 'Matthew' and last_name = 'Mahan'
and amount > 4
and return_date BETWEEN '2005-07-28' AND '2005-08-01'


#2.6.4
SELECT f.title, f.film_id
FROM customer c
JOIN payment p
ON c.customer_id = p.customer_id
JOIN rental r
ON r.rental_id = p.rental_id
JOIN inventory i
ON i.inventory_id = r.inventory_id
JOIN film f
ON f.film_id = i.film_id
WHERE f.title LIKE '%boat%' OR f.description LIKE '%boat%' 
and c.first_name = 'Matthew' and last_name = 'Mahan' and f.replacement_cost > 18

