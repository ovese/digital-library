from digital_library import DigitalLibrary
from resources import Resources
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
    
    [app_user, app_user_pwd] = my_digital_lib.user_login()
    # verify app_user is in registered list of users
    is_verified = my_digital_lib.verify_user(app_user, app_user_pwd)
    while is_verified == True:
        # print(f"Welcome {app_user}") # not needed as already referenced in main_menu function
        my_digital_lib.main_menu(app_user)
        # make selection from displayed options
        user_selection  = int(input("What library resource are you interested in: "))
        if user_selection == 1:
            my_digital_lib.register_users(app_user)
        elif user_selection == 2:
            # call the film menu selection to determine what user wants to do
            # e.g. add movie to list. borrow movie, return movie, watch movie
            # any user can only borrow, return or watch movie
            # only admin can add a movie
            my_resource.access_resource(app_user)
        elif user_selection == 3:
            exit()
        else:
            print("Unknown menu selection")
    
    
if __name__ == "__main__":
    main()