from interract_with_db import check_number_column_table, get_column_names

if __name__ == "__main__":
    print(check_number_column_table("Movies"))
    print(','.join(get_column_names("Movies")))
