from interract_with_db import *

if __name__ == "__main__":
    #create_new_row("Genres",["Horror"])
    #create_new_row("Directors",["Craven","Wes"])
    #update_new_row("Genres",["Horreeor"],4)
    #remove_new_row("Genres",4)
    print(display_table("Movies"))
    print(display_table("Directors"))
    print(display_table("Genres"))
    print(display_information_from_two_table("Movies", "Directors", 2))
    print(display_information_from_two_table("Movies", "Genres", 1))

