from digital_library import DigitalLibrary



class Resources(DigitalLibrary):
    def __init__(self, resource_name_title, resource_owner, resource_description, resource_type) -> None:
        super().__init__(resource_name_title, resource_owner, resource_description, resource_type)
        print("Inside Resources class constructor")
        
    def access_resource(self, user):
        print(f"Welcome {user}. Select from available resources: ")
        available_resources = "Welcome to the Digital Library App.\n "\
                "This app allows you to: \n"\
                "Select a resource (text or film) to use. Available resources are: \n"\
                "1. Texts (Books, journals, ) \n"\
                "2. Films (Disks, tapes, transparencies, ) \n"\
                "3. Events (Exibition, expo, ) \n"\
                "4. Return (return to main menu) \n"
        print(f"{available_resources}")
        res_selector = int(input("Select your option from the list: "))
        if res_selector == 1:
            # make a choice of text to access and how you want to access the text
            # type of text, title, author, published date
            # read, borrow, buy, donate
            # the function to be called here will come from the text resource class
            self.text_resource_menu(user)
        elif res_selector == 2:
            # access films menu
            self.film_resource_menu(user)
        elif res_selector == 3:
            # access events
            self.event_resource_menu(user)
        elif res_selector == 4:
            DigitalLibrary.main_menu(user)
        else:
            print("Unknown option selected")
            
    # define the varfious resource menus here
    def film_resource_menu(self, user):
        film_menu_list =["Add movie", "View film list", "Borrow movie", "Return movie", "Watch movie", "Purchase movie", "Donate movie"]
        # film_menu = f"Available options for movies menu include: \n"\
        #              "1. Add movie \n"\
        #              "2. View film list \n"\
        #              "3. Borrow movie \n"\
        #              "4. Return movie \n"\
        #              "5. Watch movie \n"\
        #              "6. Purchase movie \n"\
        #              "7. Donate movie \n"
        if user == "admin":
            film_menu = film_menu_list
            for i in range(len(film_menu)):
                print(f"{i+1}. {film_menu[i]}")
        elif user != "admin":
            film_menu = film_menu_list[1:]
            for i in range(len(film_menu)):
                print(f"{i+1}. {film_menu[i]}")
        
        films_menu_option = int(input("Choose movie activity to perform: "))
        if user == "admin":            
            if films_menu_option == 1:
                self.add_films_to_list(user)
            elif films_menu_option == 2:
                self.view_films_list()
            elif films_menu_option == 3:
                pass
            elif films_menu_option == 4:
                pass
            elif films_menu_option == 5:
                pass
            elif films_menu_option == 6:
                pass
            elif films_menu_option == 7:
                pass
        elif user != "admin":
            if films_menu_option == 1:
                pass
            elif films_menu_option == 2:
                pass
            elif films_menu_option == 3:
                pass
            elif films_menu_option == 4:
                pass
            elif films_menu_option == 5:
                pass
            elif films_menu_option == 6:
                pass
            
    def text_resource_menu(self, user):
        pass
    
    def event_resource_menu(self, user):
        pass

    def buy_purchase(self, resource_type):
        return super().buy_purchase(resource_type)
    
    def borrow_lease(self, resource_type):
        return super().borrow_lease(resource_type)
    
    def return_resource(self, resource_type):
        return super().return_resource(resource_type)