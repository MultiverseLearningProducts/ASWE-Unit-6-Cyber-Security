@app.route('/actors', methods=['GET'])
def get_actors():
    actor_name = request.args.get('name')
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM actor WHERE first_name = ?"
    cursor.execute(query, (actor_name,))
    rows = cursor.fetchall()
    return f"Actors: {rows}"
