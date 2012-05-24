from flask import render_template
from flask_social_auth import app

@app.route('/')
def index():
    return render_template('index.html')