from flask import render_template

def get_home():
    return render_template('index.html')
