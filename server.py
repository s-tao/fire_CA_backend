from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///fire_db'

db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Fire Data' 


if __name__ == '__main__':
    app.debug = True
    app.run()

