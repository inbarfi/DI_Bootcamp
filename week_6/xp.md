--xp

-- CREATE TABLE items(
--  id SERIAL PRIMARY KEY,
--  item VARCHAR (50) NOT NULL,
--  price smallint NOT NULL
-- );

INSERT INTO items (item, price)
VALUES
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

-- create table customers(
-- cust_id serial primary key,
-- customer_name varchar (50) not null
-- );


INSERT INTO customers (customer_name)
VALUES('Greg Jones'), ('Sandra Jones'), ('Scott Scott'), ('Trevor Green'), ('Melanie Johnson
');

select * from items;
select * from items where price > 80;
select * from items where price <= 300;
select * from customers where customer_name like '%Smith';
select * from customers where customer_name like '%Jones';
select * from customers where customer_name not like 'Scott%';
