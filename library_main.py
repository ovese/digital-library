from digital_library import DigitalLibrary
from resources import Resources
from text_resource import Texts
from film_resource import Films

# time
import time

# datetime and date
from datetime import datetime, date


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(f"Time in: {current_time}")
# Then get the current date.
curr_date = date.today()
print(f"Date: {curr_date}")

def main():
    my_digital_lib = DigitalLibrary("","","","")
    my_resource = Resources("","","","")
    my_text = Texts("","","","")
    my_film = Films("","","","")
    
    [app_user, app_user_pwd] = my_digital_lib.user_login()
    # verify app_user is in registered list of users
    is_verified = my_digital_lib.verify_user_login(app_user, app_user_pwd)
    while is_verified == True:
        # print(f"Welcome {app_user}") # not needed as already referenced in main_menu function
        my_digital_lib.main_menu(app_user)
        # make selection from displayed options
        user_selection  = int(input("Select action to perform within digital library: "))
        if user_selection == 1:
            print("Do you want to register or remove a user(yes/no)?:")
            resp = my_digital_lib.global_prompt(app_user)
            if resp == "yes":
                sel = input("Select action from below to perform\n"
                            "reg..........Register new user\n"
                            "rmv..........Remove existing user\n"
                            ":")
                if sel == "reg":
                    my_digital_lib.register_users(app_user)
                elif sel == "rmv":
                    my_digital_lib.remove_user(app_user)
            elif resp == "no":
                print("Returning to main menu...")
        elif user_selection == 2:
            # call the film menu selection to determine what user wants to do
            # e.g. add movie to list. borrow movie, return movie, watch movie
            # any user can only borrow, return or watch movie
            # only admin can add a movie
            ret_resource = my_resource.access_resource(app_user)
            if ret_resource == 1:
            # make a choice of text to access and how you want to access the text
            # type of text, title, author, published date
            # read, borrow, buy, donate
            # the function to be called here will come from the text resource class
                ret_text_menu_option = my_resource.text_resource_menu(app_user)
                my_text.text_manager(ret_text_menu_option, app_user)
            elif ret_resource == 2:
                # access films menu
                ret_film_menu_option = my_resource.film_resource_menu(app_user)
                my_film.movie_manager(ret_film_menu_option, app_user)
            elif ret_resource == 3:
                # access events
                my_resource.event_resource_menu(app_user)
            elif ret_resource == 4:
                DigitalLibrary.main_menu(app_user)
            else:
                print("Unknown option selected")
        elif user_selection == 3:
            exit()
        else:
            print("Unknown menu selection")
    
    
if __name__ == "__main__":
    main()