from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        wine = request.form['wine']
        varietal = request.form['varietal']
        origin = request.form['origin']
        year = request.form['year']
        rating = request.form['rating']
        price = request.form['price']
        yesorno = request.form['yesorno']
        comments = request.form['comments']
        #print(wine, varietal, price)
        if wine == '':
            return render_template('index.html')
        return render_template('success.html')


if __name__ == '__main__':
    app.debug = True
    app.run()