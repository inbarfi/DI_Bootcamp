# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 12:24:17 2021

@author: Inbar
"""

#xp - part2
from xp import MenuItem

# 1.1) function that creates a new MenuItem instance
def load_manager(name, price):
    new_MenuItem = MenuItem(name, price)
    return new_MenuItem

# 1.2) function that displays the program menu (not the restaurant menu!), 
# and asks the user to choose an item. 
# Call the appropriate function that matches the user’s input
def show_user_menu():
    print('MENU')
    user_choice = input('''
    (a) Add an item
    (d) Delete an Item
    (v) View the menu
    (x) Exit
    ''')
    return user_choice

# 1.3) function that asks the user to input the item’s name and price. 
# It will not interact with the menu itself, but simply call the appropriate function from the MenuItem object.
def add_item_to_menu(name, price):
    load_manager(name, price).save()
    # ? - If the item was added successfully print success: #if "select "
    print('item was added successfully.')

    
# 1.4) function that asks the user to input the name of the item they want to 
# remove from the restaurant’s menu. 
# The function should not interact with the menu itself, 
# but simply call the appropriate function from the MenuItem object.
def remove_item_from_menu(name, price = None): # what's default None?
    if load_manager(name, price).get_by_name(name):
        load_manager(name,price).delete()
        print('removed item')
    else:
        print('error')

# 1.5) print the restaurant’s menu
def show_restaurant_menu(name = None, price = None):
    load_manager(name, price).all()

def run():
    while True:
        user_choice = show_user_menu()
        if user_choice == "a" or user_choice == "d" or user_choice == "v" or user_choice == "x":
            if user_choice == "a":
                item = input('choose item name:')
                if not item.isdigit():
                    item_price = input('choose item price:')
                    add_item_to_menu(item, item_price)
                else:
                    print('invalid type')
            elif user_choice == "d":
                item = input('choose item name:')
                remove_item_from_menu(item)
            elif user_choice == "v":
                show_restaurant_menu()
            else: #x
                show_restaurant_menu()
                print('goodbye!')
                break
        else:
            print('invalid input')



run()
