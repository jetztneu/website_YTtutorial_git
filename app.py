# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 21:35:52 2024

@author: abhin
"""

from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

POEM = [
    {
        'id':'1',
        'title':'Arzee hai'
    },
    {
        'id':'2',
        'title':'Poem 2'
    },
    {
        'id':'3',
        'title':'Galti'
    }
]

BOOK = [
    {
        'id':1,
        'title':'Abhinav Anubhav',
        'year':'2010'
    },
    {
        'id':2,
        'title':'Arzee hai',
        'year': '2017'

    },
    {
        'id':3,
        'title':'Khushi ki Khoj',
        'year': '2024'
    }
]

plist = pd.read_csv('static\Poem_list.csv')

@app.route("/")
def home():
    return render_template('home.html',poem_list=POEM,book_list=BOOK,plist=plist)


@app.route("/api/books")
def list_books():
    return jsonify(BOOK)