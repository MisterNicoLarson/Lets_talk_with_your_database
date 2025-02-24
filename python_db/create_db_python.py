import sqlite3

conn = sqlite3.connect("database_movie.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Genres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Directors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        last_name TEXT NOT NULL,
        first_name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        release_year INTEGER NOT NULL,
        genre_id INTEGER,
        director_id INTEGER,
        FOREIGN KEY (genre_id) REFERENCES Genres(id),
        FOREIGN KEY (director_id) REFERENCES Directors(id)
    )
''')

cursor.execute("INSERT INTO Genres (name) VALUES ('Biopic')")
cursor.execute("INSERT INTO Genres (name) VALUES ('Comedy')")
cursor.execute("INSERT INTO Genres (name) VALUES ('Action')")

cursor.execute("SELECT id FROM Genres WHERE name = 'Biopic'")
gen1 = cursor.fetchone()[0]

cursor.execute("SELECT id FROM Genres WHERE name = 'Comedy'")
gen2 = cursor.fetchone()[0]

cursor.execute("SELECT id FROM Genres WHERE name = 'Action'")
gen3 = cursor.fetchone()[0]

cursor.execute("INSERT INTO Directors (last_name, first_name) VALUES ('Mangold', 'James')")
cursor.execute("INSERT INTO Directors (last_name, first_name) VALUES ('Reitman', 'Ivan')")

cursor.execute("SELECT id FROM Directors WHERE last_name = 'Mangold'")
jm1 = cursor.fetchone()[0]

cursor.execute("SELECT id FROM Directors WHERE last_name = 'Reitman'")
ir1 = cursor.fetchone()[0]

cursor.execute("INSERT INTO Movies (title, release_year, genre_id, director_id) VALUES ('Walk the Line', 2005, ?, ?)", (gen1, jm1))
cursor.execute("INSERT INTO Movies (title, release_year, genre_id, director_id) VALUES ('A Complete Unknown', 2024, ?, ?)", (gen1, jm1))
cursor.execute("INSERT INTO Movies (title, release_year, genre_id, director_id) VALUES ('Night and Day', 2010, ?, ?)", (gen3, jm1))
cursor.execute("INSERT INTO Movies (title, release_year, genre_id, director_id) VALUES ('Twins', 1988, ?, ?)", (gen2, ir1))
cursor.execute("INSERT INTO Movies (title, release_year, genre_id, director_id) VALUES ('Ghostbusters', 1984, ?, ?)", (gen2, ir1))
cursor.execute("INSERT INTO Movies (title, release_year, genre_id, director_id) VALUES ('Six Days Seven Nights', 1998, ?, ?)", (gen2, ir1))

conn.commit()
conn.close()

print("Database and data inserted successfully!")
