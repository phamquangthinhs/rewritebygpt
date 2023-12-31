# -*- coding: utf-8 -*-

import os, sys, json
from flask import Flask, request, flash, url_for, \
    redirect, render_template, session, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'adambaylin'

@app.route('/')
def homepage():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)