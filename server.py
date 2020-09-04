from flask import Flask
from model import db

app = Flask(__name__)



@app.route('/')
def index():
    return 'Fire Data' 


if __name__ == '__main__':
    app.debug = True
    app.run()

    postgresql://fire_db