import sqlite3


connect = sqlite3.connect("movies.db")
cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies(
            name TEXT NOT NULL,
            genre VARCHAR(80) NOT NULL,
            rating INTEGER 
        )
''')
connect.commit()

def create_movie(name,genre,rating=None):
    cursor.execute(
        'INSERT INTO movies(name, genre, rating) VALUES (?,?,?)',
        (name, genre, rating)
    )
    connect.commit()
    print(f"Фильм {name} добавлен!")

# create_movie("Blonde in law", "Comedy", 8.9)

def get_movie():
    cursor.execute('SELECT * FROM movies')
    movies = cursor.fetchall()
    for i in movies:
        print(f"NAME: {i[0]} GENRE: {i[1]} RATING: {i[2]}")
# get_movie()

def update_movie(row_id, name, genre, rating):
    cursor.execute(
        'UPDATE movies SET name=?, genre=?, rating=? WHERE rowid=? ',
        (name, genre, rating, row_id)
                    )
    connect.commit()
    print("Фильм обновлён!")

# update_movie(3, "Scream", "Horror", 9.5)

def delete_movie(row_id):
    cursor.execute(
        'DELETE FROM movies WHERE ROWID=?',
        (row_id,)
    )
    connect.commit()
    print("Фильм удалён!")
# delete_movie(1)

def get_by_rowid(row_id):
    cursor.execute(
        'SELECT * FROM movies WHERE rowid=?',
        (row_id,)
    )
    print(cursor.fetchone())
get_by_rowid(2)