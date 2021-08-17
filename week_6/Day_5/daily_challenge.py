# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 12:36:49 2021

@author: Inbar
"""

#daily_chalenge

import requests
import random
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
#insert my password
PASSWORD = '' 
DATABASE = 'countries'
#https://restcountries.eu/rest/v2/all
connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
cursor = connection.cursor()

def get_random_data():
    response = requests.get("https://restcountries.eu/rest/v2/all")
    data = response.json() 
    #print(response)
    for _ in range(10):
        x = random.choice(data)
        save_q = f"insert into items (name, capital, flag, subregion, population) values(\'{x['name']}\', \'{x['capital']}\', \'{x['flag']}\', \'{x['subregion']}\', {x['population']});"
        cursor.execute(save_q)
        connection.commit()

get_random_data()
