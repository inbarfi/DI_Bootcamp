# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:35:56 2021

@author: Inbar
"""

CREATE DATABASE supermarket;
CREATE TABLE items(
item_id SERIAL NOT NULL, title VARCHAR(250) NOT NULL, price INT, last_update TIMESTAMP,
PRIMARY KEY (item_id)
)

SELECT * FROM items

CREATE TABLE orders(
order_id INT NOT NULL, user_id INT NOT NULL, item_id INT NOT NULL, price INT NOT NULL,
last_update TIMESTAMP, FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE,
FOREIGN KEY (item_id) REFERENCES items (item_id) ON DELETE CASCADE
);

CREATE TABLE users(
user_id SERIAL NOT NULL, first_name VARCHAR(250) NOT NULL, last_name VARCHAR(250) NOT NULL, 
email VARCHAR(250) NOT NULL, last_update TIMESTAMP, PRIMARY KEY (user_id)
);

SELECT * FROM ORDERS
SELECT * FROM users

CREATE or REPLACE FUNCTION user_orders(ord INT, usr VARCHAR (250)) 
RETURNS INT AS $totalprice$ 
BEGIN
    RETURN(SELECT price FROM orders INNER JOIN users ON users.user_id = orders.user_id
    INNER JOIN items ON items.item_id = orders.item_id WHERE orders.order_id = ord AND
    users.last_name = usr);
END;
$totalprice$ LANGUAGE plpgsql;

INSERT INTO orders(order_id, user_id, item_id, price, last_update) 
VALUES(1, 1, 1, 500, '1970-01-01 00:00:00');

INSERT INTO users(user_id, first_name, last_name, email, last_update) 
VALUES('Geotge', 'Clooney', 'georgeclooney@aaa.com', '1970-01-01 00:00:00');

INSERT INTO orders(order_id, user_id, item_id, price, last_update) 
VALUES(1, 1, 1, 500, '1970-01-01 00:00:00');

SELECT * FROM user_orders(1, 'Clooney');
 
