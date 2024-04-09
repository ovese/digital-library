"""This project is meant to simulate the operations of a Digital Library.
The program is structured using all core tools of OOP, SOLID and best practice.
The Digital Library organizational flow is as described:
class DigitalLibrary is main or parent class

class Resource inherits from DigitalLibrary as a subclass
class Text inherits from Resource
class Films inherits from Resource

class Books, Journals, Newspapers inherits from Text

The applications will have two types of users: 
Admin and ordinary user.
Acces to library resources will be determined by user type such that
menu items on display is tied to logged in user.

Ordinary users can have a subscription of 6 months or 1 year"""

import os

class DuplicateEntryError(Exception):
    pass

class DigitalLibrary:
    def __init__(self, resource_name_title, resource_owner, resource_description, resource_type ) -> None:
        print("Inside parent project class or DigitalLibrary constructor")
        self.resource_name_title =  resource_name_title
        self.resource_owner =  resource_owner
        self.resource_description =  resource_description
        self.resource_type = resource_type
        
    def global_prompt(self, user):
        instant_response = input("yes or no?: ").lower()
        
        return instant_response
        
        
    def user_login(self):
        x_user = input("Enter username: ")
        x_password = input("Enter password: ")
        
        return x_user, x_password
    
    def verify_user_login(self, inst_username, inst_pwd):
        access_granted = False
        user_file_contents = ""
        with open("users_file.txt", "r") as user_details:
            user_file_contents = user_details.readlines()
        # print(type(user_file_contents))
        # print(user_file_contents)
        
        # I am going to take each string, strip the \n char then extract part i need
        user_name_list = []
        pwd_list = []
        for i, item in enumerate(user_file_contents):
            # print(item.strip().split(','))
            user_name_list.append(item.strip().split(',')[0])
            pwd_list.append(item.strip().split(',')[1])
        # print(f"debug...{user_name_list})
        # print(f"debug...........{pwd_list})
        if((inst_username in user_name_list) and (inst_pwd in pwd_list)):
            print("Verification complete")
            access_granted = True
        else:
            print("Unable to verify user details. Incorrect or non-existent user details entered")
            access_granted = False
        
        return access_granted
    
    def main_menu(self, inst_user):
        welcome_text = f"Welcome {inst_user}, to the Digital Library App.\n"\
                        "1. Register/remove user \n"\
                        "2. Access library resource \n"\
                        "3. Exit \n"
        print(welcome_text)
        
    def verify_reg_user(self, inst_username, inst_pwd):
        # ensure the registration details are unique
        pass

    def register_users(self, user):
        # check is user_file exists at start and creat one if not in existence
        if not os.path.exists("users_file.txt"):
            with open("users_file.txt", "w") as default_user_file:
                pass
        # verify the logged in user as admin to carry out this operation
        # of user registration 
        if user == "admin":
            try:
                user_name = input("Enter username: ")
                password = input("Enter password: ")
                subscription_type = input("Enter subscription type(basic, unlimited): ")
                subscription_duration = input("Enter duration of subscription(6 or 12 months): ")
                user_dict = {}
                user_dict["user_name"] = user_name
                user_dict["password"] = password
                user_dict["sub_type"] = subscription_type
                user_dict["sub_duration"] = subscription_duration
                
                # see what the dictionary contents looks like
                print(user_dict)
                user_key = user_dict.keys()
                user_val = user_dict.values()
                print(f"user keys: {type(user_key)}....{user_key}")
                print(f"user values: {type(user_val)}...{user_val}")
                # write contents of dictionary to file as string
                # intermediate conversion to list before string conversion
                user_entry = (',').join(list(user_val))
                print(f"{type(user_entry)}: {user_entry}")                  
                with open("users_file.txt", "a") as library_users_file:
                    library_users_file.write(user_entry+'\n')
            except ValueError as ve:
                print(ve)
            except DuplicateEntryError as deerr:
                print(deerr)
            else:
                pass
            finally:
                pass
        else:
            print("Sorry you are not authorised to register a user")
            
    def remove_user(self, user):
        pass
        
    def buy_purchase(self, resource_type):
        self.resource_type =  resource_type
        
    def borrow_lease(self, resource_type):
        self.resource_type = resource_type
        
    def return_resource(self, resource_type):
        self.resource_type = resource_type
        
    def host_event(self, event_type):
        self.resource_type = event_type


        
        