# 📌 Introduction

In this project, I will work with databases using three programming languages: Python, Java, and C#. The goal is to gain hands-on experience in connecting to a database, performing CRUD (Create, Read, Update, Delete) operations, and manipulating data efficiently in each language.

To achieve this, I will create a Movie Management 🎬 database using SQLite. This database will store information about movies, genres, and directors. Then, I will implement various operations in Python, Java, and C# to interact with the database, including adding, searching, updating, and deleting records.

Through this project, I will improve my database handling skills, understand how different languages interact with databases, and practice writing efficient SQL queries. 🚀

#📌 Database Concept

We will work with a Movie Management 🎬 database with the following tables:

    Movies (id, title, release_year, genre_id, director_id)
    Genres (id, name)
    Directors (id, last_name, first_name)

# 1. Creating the Database
SQL - Table Creation

CREATE TABLE Genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE Directors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name TEXT NOT NULL,
    first_name TEXT NOT NULL
);

CREATE TABLE Movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    release_year INTEGER NOT NULL,
    genre_id INTEGER,
    director_id INTEGER,
    FOREIGN KEY (genre_id) REFERENCES Genres(id),
    FOREIGN KEY (director_id) REFERENCES Directors(id)
);

Sample Data Insertions

INSERT INTO Genres (name) VALUES ('Action'), ('Comedy'), ('Drama');

INSERT INTO Directors (last_name, first_name) VALUES ('Nolan', 'Christopher'), ('Tarantino', 'Quentin');

INSERT INTO Movies (title, release_year, genre_id, director_id) VALUES 
('Inception', 2010, 1, 1), 
('Pulp Fiction', 1994, 2, 2);

# 2. Exercises to Implement in Python, Java, and C#

The goal is to manipulate this database using these three languages.
💡 Exercise 1: Connect to the Database

    Establish a connection with SQLite and display all movies.

💡 Exercise 2: Add a Movie

    Ask the user to input a new movie (title, release year, genre, director) and insert it into the database.

💡 Exercise 3: Search for a Movie

    Allow the user to search for a movie by title.

💡 Exercise 4: Update a Movie

    Modify the release year of a given movie.

💡 Exercise 5: Delete a Movie

    Delete a movie based on its ID.
