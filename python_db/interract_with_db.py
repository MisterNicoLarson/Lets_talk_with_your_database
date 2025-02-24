import sqlite3
def create_new_row(table, l_info, database="database_movie.db"):
    """
    Insert a new row into a specified table within a SQLite database.

    Parameters:
    table (str): The name of the table to insert the new row into.
    l_info (list): A list of values to be inserted into the new row. The length of this list must match the number of columns in the table.
    database (str): The name of the SQLite database file. Default is "database_movie.db".

    Returns:
    bool: True if the row was inserted, False otherwise.

    This function retrieves the column names of the specified table and checks if the length of the provided list of values matches the number of columns. If they match, it constructs an SQL INSERT query and executes it to insert the new row. If the row already exists, it prints a message.
    """
    conn = None
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        columns = get_column_names(table)

        if len(l_info) != len(columns):
            print(f"The number of values ({len(l_info)}) does not match the number of columns ({len(columns)}) in {table}.")
            return False

        if check_if_row_already_in_db(l_info, table, database):
            print("The row is already in the database.")
            return False

        placeholders = ", ".join(["?"] * len(l_info))
        query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})"
        
        cursor.execute(query, l_info)
        conn.commit()
        
        print(f"New row inserted successfully into {table}!")
        return True

    except sqlite3.Error as e:
        print(f"Error inserting data into {table}: {e}")
        return False

    finally:
        if conn:
            conn.close()


def update_new_row(table,l_info,id_update):
    return 0

def remove_new_row(table,l_info,id_update):
    return 0

def check_number_column_table(table, database="database_movie.db"):
    """
    Check the number of columns in a specified table within a SQLite database.

    Parameters:
    table (str): The name of the table to check.
    database (str): The name of the SQLite database file. Default is "database_movie.db".

    Returns:
    int: The number of columns in the specified table.
    """
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM pragma_table_info('{table}')")
    table_info = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return table_info

def get_column_names(table, database="database_movie.db"):
    """
    Retrieve the column names of a specified table within a SQLite database.

    Parameters:
    table (str): The name of the table to retrieve column names from.
    database (str): The name of the SQLite database file. Default is "database_movie.db".

    Returns:
    list: A list of column names in the specified table.
    """
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table})")
    columns = [row[1] for row in cursor.fetchall()]
    conn.close()
    return columns

def check_if_row_already_in_db(new_row, table, database="database_movie.db"):
    """
    Check if a given row already exists in a specified table within a SQLite database.

    Parameters:
    new_row (list): A list of values representing the new row to check.
    table (str): The name of the table to check for the existence of the row.
    database (str): The name of the SQLite database file. Default is "database_movie.db".

    Returns:
    bool: True if the row already exists in the table, False otherwise.

    This function retrieves all rows from the specified table and compares each row with the provided new row. Both the existing rows and the new row are normalized by trimming whitespace and converting to lowercase before comparison. If a match is found, the function returns True; otherwise, it returns False.
    """
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()

        for elt in rows:
            
            normalized_db_row = [str(value).strip().lower() for value in elt]
            normalized_new_row = [str(value).strip().lower() for value in new_row]

            if normalized_db_row == normalized_new_row:
                return True  

        return False 

    except sqlite3.Error as e:
        print(f"❌ Error checking row in {table}: {e}")
        return False

    finally:
        conn.close()
