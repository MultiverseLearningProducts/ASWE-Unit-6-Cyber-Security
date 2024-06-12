
from flask import Flask, request, g
import sqlite3

app = Flask(__name__)
DATABASE = r'C:\Users\mwasha.mutale\Downloads\archive\sqlite-sakila-db\sqlite-sakila.sq'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return 'Welcome to the example app using the Sakila database!'

@app.route('/actors', methods=['GET'])
def get_actors():
    actor_name = request.args.get('name')
    db = get_db()
    cursor = db.cursor()
    query = f"SELECT * FROM actor WHERE first_name = '{actor_name}'"
    cursor.execute(query)
    rows = cursor.fetchall()
    return f"Actors: {rows}"

if __name__ == '__main__':
    app.run(debug=True, port=8080)
