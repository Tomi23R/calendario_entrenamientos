from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/create_training', methods=['POST'])
def create_training():
    if request.method == 'POST':
        return
    else:
        return
