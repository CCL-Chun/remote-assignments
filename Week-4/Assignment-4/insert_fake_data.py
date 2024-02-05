import os
import pymysql
import random
from dotenv import load_dotenv
from faker import Faker

# load .env for database parameters
load_dotenv()
# Get database configuration
MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DB = os.environ.get('MYSQL_DB')

def connect_db():
    """Connect to the MySQL database"""
    database = pymysql.connect(host = MYSQL_HOST,
                            user = MYSQL_USER,
                            password = MYSQL_PASSWORD,
                            database = MYSQL_DB,
                            cursorclass = pymysql.cursors.DictCursor)
    return database

db = connect_db()
cursor = db.cursor()
fake = Faker()

# There are 6 id in user table from assignment-3
user_ids = list(range(1, 7))

# Generate 30 fake articles
for _ in range(30):
    title = fake.sentence(nb_words=10)  # fake title
    content = fake.text(max_nb_chars=1000)  # fake article content
    author_id = random.choice(user_ids)  # Randomly choose an author_id
    # INSERT fake data into database
    cursor.execute('INSERT INTO article VALUES (NULL, %s, %s, %s)',
                   (title, content, author_id,))# tuple here
db.commit() #commit the changes is important

# select all articles with their author’s email
# cursor.execute('SELECT A.title, A.content, U.email FROM article A \
#                JOIN user U ON U.id = A.author_id')

# select articles from 7th to 12th sorted by id.
# cursor.execute('SELECT * FROM article\
#                WHERE id BETWEEN 7 and 12\
#                ORDER BY id')
# alternative
# cursor.execute('SELECT * FROM article \
#                 ORDER BY id \
#                 LIMIT 6 OFFSET 6')

db.close()
