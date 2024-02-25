# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 21:35:52 2024

@author: abhin
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')