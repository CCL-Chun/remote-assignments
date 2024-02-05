import configparser
from flask import Flask, g
import pymysql

app = Flask(__name__)

# Read configuration file
config = configparser.ConfigParser()
config.read('config.ini')
# Get database configuration
app.config['MYSOL_HOST'] = config.get('mysql', 'host')
app.config['MYSOL_USER'] = config.get('mysql', 'user')
app.config['MYSOL_PASSWORD'] = config.get('mysql', 'password')
app.config['MYSOL_DB'] = config.get('mysql', 'db')

def get_db():
    """Connect to the MySQL database"""
    if 'db' not in g:
        g.db = pymysql.connect(host=app.config['MYSOL_HOST'],
                               user=app.config['MYSOL_USER'],
                               password=app.config['MYSOL_PASSWORD'],
                               database=app.config['MYSOL_DB'],
                               cursorclass=pymysql.cursors.DictCursor)
        return g.db

@app.teardown_appcontext
def close_db(error):
    """
    to ensure the database connection is closed at the end of each request,
    cleaning up resources and preventing leaks.
    """
    #close database at the end of request
    db = g.pop('db', None)
    if db is not None:
        db.close()

from app import routes
