# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 21:03:08 2021

@author: Inbar
"""

--xp
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










