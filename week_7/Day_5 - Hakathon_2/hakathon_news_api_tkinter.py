# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 11:53:22 2021

@author: Inbar
"""
# getting top headlines from TechCrunch right now
import requests
import tkinter as tk

def get_news():
    api_key = "23e7f1a1d133415e8c5f062d5dc3ef2e"
    url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="+api_key
    news = requests.get(url).json()
    articles = news["articles"]
    my_articles = []
    my_news = ""
    for article in articles:
        my_articles.append(article["title"])
    for i in range(10):
        my_news = my_news + str(i+1) + ". " + my_articles[i] + "\n"
    
    #print(my_news)
    label.config(text = my_news)
    
#tinker window:    
canvas = tk.Tk()
canvas.geometry("900x600")
canvas.title("News App")

button = tk.Button(canvas, font = 24, text = "Reload", command = "getNews")
button.pack(pady = 20)

label = tk.Label(canvas, font = 18, justify = "left")
label.pack(pady = 20)

get_news()
canvas.mainloop()
