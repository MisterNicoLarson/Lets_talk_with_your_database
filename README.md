# 🎬 Movie Database Project  

## 📌 Introduction  

In this project, I will work with **databases** using three programming languages: **Python, Java, and C#**. The objective is to gain **hands-on experience** in database interactions, perform **CRUD** (Create, Read, Update, Delete) operations, and efficiently manipulate data using different languages.  

To accomplish this, I will design a **Movie Management** database using **SQLite**. This database will store details about **movies, genres, and directors**. Using Python, Java, and C#, I will implement various functionalities, including:  
✅ Adding new movies  
✅ Searching for movies  
✅ Updating movie details  
✅ Deleting movies  

By completing this project, I will enhance my **database management skills**, explore how different languages interact with databases, and practice writing optimized **SQL queries**. 🚀  

---

## 📌 Database Structure  

The **Movie Management** database consists of the following three tables:  

### **🎥 Movies**  
Stores details of each movie.  
- `id` (INTEGER, Primary Key)  
- `title` (TEXT, Movie title)  
- `release_year` (INTEGER, Year of release)  
- `genre_id` (INTEGER, Foreign Key → Genres table)  
- `director_id` (INTEGER, Foreign Key → Directors table)  

### **🎭 Genres**  
Stores different movie genres.  
- `id` (INTEGER, Primary Key)  
- `name` (TEXT, Genre name)  

### **🎬 Directors**  
Stores details of movie directors.  
- `id` (INTEGER, Primary Key)  
- `last_name` (TEXT, Director's last name)  
- `first_name` (TEXT, Director's first name)  

---

## 📌 1. Creating the Database  

### **SQL - Table Creation**  

```sql
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
```

### Sample Data Insertions
```sql

INSERT INTO Genres (name) VALUES ('Action'), ('Comedy'), ('Drama');

INSERT INTO Directors (last_name, first_name) VALUES ('Nolan', 'Christopher'), ('Tarantino', 'Quentin');

INSERT INTO Movies (title, release_year, genre_id, director_id) VALUES 
('Inception', 2010, 1, 1), 
('Pulp Fiction', 1994, 2, 2);
```

## 📌 2. Exercises: Implementing in Python, Java, and C#

The goal is to manipulate this database using three different programming languages: Python, Java, and C#.
💡 Exercise 1: Connect to the Database

    Establish a connection with SQLite.
    Retrieve and display all movies.

💡 Exercise 2: Add a Movie

    Ask the user for movie details (title, release year, genre, director).
    Insert the new movie into the database.

💡 Exercise 3: Search for a Movie

    Allow the user to search for a movie by title.
    Display the results.

💡 Exercise 4: Update a Movie

    Modify the release year of a given movie.

💡 Exercise 5: Delete a Movie

    Remove a movie based on its ID.
