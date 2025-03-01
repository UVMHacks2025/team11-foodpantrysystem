from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route('/', methods = ['Post', 'Get'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8005)