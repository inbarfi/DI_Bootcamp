# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 21:03:08 2021

@author: Inbar
"""

#xp
#1
select * from items
order by price;

select * from items
where price >= 80
order by price desc;

select customer_name from customers
order by customer_name 
limit 3;

select customer_name from customers
order by customer_name desc;

 CREATE TABLE purchases(
 customer_id SERIAL,
 item_id SERIAL,
 FOREIGN KEY (customer_id) REFERENCES customers (cust_id),
 FOREIGN KEY (item_id) REFERENCES customers (cust_id)
);

insert into purchases (customer_id, item_id) values
(2,2), (3,3), (4,4), (5,5);

select * from customers c
inner join purchases p
on c.cust_id = p.customer_id;

select * from customers c
inner join purchases p
on c.cust_id = p.customer_id
where cust_id = 4;

select * from items i
inner join purchases p
on i.id = p.customer_id
where item = 'Large Desk' or item = 'Small Desk';

#1.4
insert into items(item,price) values ('Hard Drive', 500);
insert into purchases (customer_id, item_id) 
values ((select cust_id from customers where customer_name = 'Scott Scott'),
	   (select id from items where item = 'Hard Drive'));

#1.5
select customer_name FROM customers c
INNER JOIN purchases p 
ON c.cust_id = p.customer_id;

select customer_name, item FROM customers c
INNER JOIN purchases p 
ON c.cust_id = p.customer_id
INNER JOIN items i 
ON i.id = p.customer_id;

#2.1
SELECT *
FROM customers
#2.2
SELECT concat(first_name, ' ', last_name) full_name
FROM customer
#2.3
SELECT DISTINCT create_date
FROM customer
#2.4
SELECT *
FROM customer 
ORDER BY first_name DESC
#2.5
SELECT film_id, title, description, release_year, rental_rate
FROM film 
ORDER BY rental_rate
#2.6
SELECT address, phone
FROM address
WHERE district = 'Texas'
#2.7
SELECT *
FROM film
WHERE film_id in (15, 150)
#2.8
SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title = 'Ali forever' or title = 'Ali Forever'
#2.9
SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title LIKE 'Al%' or title LIKE 'al%'
#2.10
SELECT *
FROM payment
WHERE amount != 0
ORDER BY amount ASC
LIMIT 10
#2.11 - ?
#2.12
SELECT amount, payment_date
FROM customer c
JOIN payment p
ON c.customer_id = p.customer_id
ORDER BY payment_id
#2.13
SELECT title, film_id 
FROM film 
WHERE film_id not in (select film_id from inventory)
#2.14
SELECT country, city
FROM city
JOIN country
ON city.country_id = country.country_id
WHERE city.country_id = country.country_id
#add window to get partition by country (and all cities inside it)
#2.15 - not the same result for count id when joining directly or not directly using rental
SELECT c.customer_id, first_name, last_name
FROM customer c
-- JOIN rental r
-- ON r.customer_id = c.customer_id
JOIN payment p
ON p.customer_id = c.customer_id
