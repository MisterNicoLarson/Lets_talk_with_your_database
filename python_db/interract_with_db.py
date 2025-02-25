import sqlite3

def create_new_row(table, l_info, database="database_movie.db"):
    """
    Insert a new row into a specified table within a SQLite database.

    Parameters:
    table (str): The name of the table to insert the new row into.
    l_info (list): A list of values to be inserted into the new row. The length of this list must match the number of columns in the table, excluding the auto-incremented 'id' column.
    database (str): The name of the SQLite database file. Default is "database_movie.db".

    Returns:
    bool: True if the row was inserted, False otherwise.
    """
    try:
        with sqlite3.connect(database) as conn:
            cursor = conn.cursor()

            columns = get_column_names(table)
            if len(l_info) != len(columns) - 1:
                print(f"The number of values ({len(l_info)}) does not match the number of columns ({len(columns) - 1}) in {table}, excluding the 'id' column.")
                return False

            columns_to_insert = columns[1:]

            if check_if_row_already_in_db(l_info, table, database):
                print("The row is already in the database.")
                return False

            placeholders = ", ".join(["?"] * len(l_info))
            query = f"INSERT INTO {table} ({', '.join(columns_to_insert)}) VALUES ({placeholders})"

            cursor.execute(query, l_info)
            conn.commit()

            print(f"New row inserted successfully into {table}!")
            return True

    except sqlite3.Error as e:
        print(f"Error inserting data into {table}: {e}")
        return False


def update_new_row(table, update_row, id_update, database="database_movie.db"):
    """
    Update a row in a specified table within a SQLite database.

    Parameters:
    table (str): The name of the table to update.
    update_row (list): A list of values to update the row with. The length of this list must match the number of columns in the table, excluding the 'id' column.
    id_update (int): The ID of the row to update.
    database (str): The name of the SQLite database file. Default is "database_movie.db".

    Returns:
    bool: True if the update was successful, False otherwise.

    This function retrieves the column names of the specified table and checks if the length of the provided list of values matches the number of columns, excluding the 'id' column. If they match, it constructs an SQL UPDATE query and executes it to update the specified row. If the lengths do not match, it prints an error message and returns False.
    """
    try:
        with sqlite3.connect(database) as conn:
            cursor = conn.cursor()

            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,))
            if not cursor.fetchone():
                print(f"Table '{table}' does not exist.")
                return False

            cursor.execute(f"SELECT id FROM {table} WHERE id = ?", (id_update,))
            if not cursor.fetchone():
                print(f"Row with ID {id_update} does not exist in {table}.")
                return False

            columns = get_column_names(table)
            if len(update_row) != len(columns) - 1:
                print(f"The number of values ({len(update_row)}) does not match the number of columns ({len(columns) - 1}) in {table}, excluding the 'id' column.")
                return False

            columns_to_update = columns[1:]  
            set_clause = ", ".join([f"{column} = ?" for column in columns_to_update])
            query = f"UPDATE {table} SET {set_clause} WHERE id = ?"

            cursor.execute(query, update_row + [id_update])
            conn.commit()
            print(f"Row with ID {id_update} updated successfully in {table}!")
            return True

    except sqlite3.Error as e:
        print(f"Error updating row in {table}: {e}")
        return False

def remove_new_row(table, id_row_to_remove, database="database_movie.db"):
    """
    Remove a row from a specified table within a SQLite database.

    Parameters:
    table (str): The name of the table from which to remove the row.
    id_row_to_remove (int): The ID of the row to remove.
    database (str): The name of the SQLite database file. Default is "database_movie.db".

    Returns:
    bool: True if the row was removed successfully, False otherwise.

    This function constructs an SQL DELETE query to remove the row with the specified ID from the specified table. It commits the change to the database and closes the connection.
    """
    try:
        with sqlite3.connect(database) as conn:
            cursor = conn.cursor()

            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,))
            if not cursor.fetchone():
                print(f"Table '{table}' does not exist.")
                return False

            cursor.execute(f"SELECT id FROM {table} WHERE id = ?", (id_row_to_remove,))
            if not cursor.fetchone():
                print(f"Row with ID {id_row_to_remove} does not exist in {table}.")
                return False

            cursor.execute(f"DELETE FROM {table} WHERE id = ?", (id_row_to_remove,))
            conn.commit()
            print(f"Row with ID {id_row_to_remove} removed successfully from {table}!")
            return True

    except sqlite3.Error as e:
        print(f"Error removing row from {table}: {e}")
        return False

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
    """
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()

        for elt in rows:
            normalized_db_row = [str(value).strip().lower() for value in elt[1:]]  # Exclude the 'id' column
            normalized_new_row = [str(value).strip().lower() for value in new_row]

            if normalized_db_row == normalized_new_row:
                return True

        return False

    except sqlite3.Error as e:
        print(f"Error checking row in {table}: {e}")
        return False

    finally:
        conn.close()

def display_table(table, id=None, database="database_movie.db"):
    """
    Display all rows from a given table with properly aligned columns.
    
    Parameters:
    table (str): The name of the table to display.
    id (int, optional): The specific ID to filter by. Default is None (display all).
    database (str): The name of the SQLite database file.

    Returns:
    str: A formatted string of the table rows with aligned column names.
    """
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    try:
        column_names = get_column_names(table, database)

        if id is not None:
            query = f"SELECT * FROM {table} WHERE id = ?"
            cursor.execute(query, (id,))
        else:
            query = f"SELECT * FROM {table}"
            cursor.execute(query)

        rows = cursor.fetchall()

        if not rows:
            return f"No records found in table '{table}'."

        col_widths = [max(len(str(col)), max(len(str(row[i])) for row in rows)) for i, col in enumerate(column_names)]

        header = " | ".join(col.ljust(col_widths[i]) for i, col in enumerate(column_names))
        separator = "-+-".join("-" * col_widths[i] for i in range(len(column_names)))

        formatted_rows = [header, separator]
        for row in rows:
            formatted_rows.append(" | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))))

        return "\n".join(formatted_rows)

    except sqlite3.Error as e:
        return f"Error fetching data from {table}: {e}"

    finally:
        conn.close()


def display_information_from_two_table(table_1, table_2, id, database="database_movie.db"):
    """
    Display information from two related tables using a JOIN operation.

    Parameters:
    table_1 (str): The main table containing the foreign key.
    table_2 (str): The second table to join.
    id (int): The ID corresponding to the foreign key (e.g., genre_id or director_id).
    database (str): The SQLite database file. Default is "database_movie.db".

    Returns:
    str: A formatted string displaying the joined data.
    """
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    try:
        foreign_key_mapping = {
            "Genres": "genre_id",
            "Directors": "director_id"
        }

        if table_2 not in foreign_key_mapping:
            return f"Table '{table_2}' is not linked to '{table_1}' by a known foreign key."

        foreign_key = foreign_key_mapping[table_2]

        cursor.execute(f"PRAGMA table_info({table_1})")
        columns_1 = [row[1] for row in cursor.fetchall()]

        cursor.execute(f"PRAGMA table_info({table_2})")
        columns_2 = [row[1] for row in cursor.fetchall()]

        query = f"""
        SELECT {', '.join([f"{table_1}.{col}" for col in columns_1])}, 
               {', '.join([f"{table_2}.{col}" for col in columns_2])}
        FROM {table_1}
        INNER JOIN {table_2} ON {table_1}.{foreign_key} = {table_2}.id
        WHERE {table_1}.{foreign_key} = ?
        """

        cursor.execute(query, (id,))
        rows = cursor.fetchall()

        if not rows:
            return f"No records found for {foreign_key} = {id} in {table_1}."

        all_columns = columns_1 + columns_2
        formatted_rows = [" | ".join(col.ljust(15) for col in all_columns)]  
        formatted_rows.append("-+-".join("-" * 15 for _ in all_columns))  

        for row in rows:
            formatted_rows.append(" | ".join(str(val).ljust(15) for val in row))  

        return "\n".join(formatted_rows)

    except sqlite3.Error as e:
        return f"Error fetching data from {table_1} and {table_2}: {e}"

    finally:
        conn.close()
