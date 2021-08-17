# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 12:23:39 2021

@author: Inbar
"""

#xp - part1 
#creating a table in postgre sql:
# =============================================================================
# CREATE TABLE menu(
#  dish_id SERIAL PRIMARY KEY,
#  dish_name VARCHAR (50),
#  price integer
# )
# =============================================================================
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'enbar007'
DATABASE = 'public'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
cursor = connection.cursor()

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def save(self): 
        query = f"INSERT INTO menu(dish_name, price) VALUES ('{self.name}', {self.price});"
        #self.run_query()
        cursor.execute(query)
        connection.commit()
        print('dish was added successfully.')   
    def delete(self):
        query = f"delete from menu where dish_name = '{self.name}';"
        #self.run_query()
        cursor.execute(query)
        connection.commit()
    def update(self, item, price):
        query = f"update menu set dish_name ='{self.name}', price = {self.price} where dish_name = '{self.name}'"
        #self.run_query()
        cursor.execute(query)
        connection.commit()
    def all(self):
        query = f"select * from menu;" 
        cursor.execute(query)
        results = cursor.fetchall()
        for item in results:
            return item 
    #@staticmethod
    def get_by_name(self, name):
        query = f"select dish_name from menu where dish_name = '{name}';"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result, "printed")
        if result: #empty = False
            for item in result:
                return item
        else:
            return None
    def run_query(self, query):
        cursor.execute(query)
        #commit
        connection.commit()
        # closing the connection
        connection.close()   
        
       
item = MenuItem('Burger', 35)
item.save()
#item.delete()
item.update('Veggie Burger', 37)
#item2 = MenuItem.get_by_name('Beef Stew')
#items = MenuItem.all()
item.get_by_name('pizza')
        
# =============================================================================
# x = []
# print(len(x))
# =============================================================================
        
        