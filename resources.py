from digital_library import DigitalLibrary

# Next 2 lines were removed on account of fixing circular import issue
# from text_resource import Texts  
# from film_resource import Films


class Resources(DigitalLibrary):
    def __init__(self, resource_name_title, resource_owner, resource_description, resource_type) -> None:
        super().__init__(resource_name_title, resource_owner, resource_description, resource_type)
        print("Inside Resources class constructor")
        
    def access_resource(self, user):
        print(f"Welcome {user}. Select from available resources: ")
        available_resources = "Welcome to the Digital Library App.\n "\
                "This app allows you to: \n"\
                "Select a resource (text or film) to use. Available resources are: \n"\
                "1. Texts (Books, journals, manuscripts) \n"\
                "2. Films (Disks, tapes, transparencies, ) \n"\
                "3. Events (Exibition, expo, ) \n"\
                "4. Return (return to main menu) \n"
        print(f"{available_resources}")
        res_selector = int(input("Select your option from the list: "))
            
        return res_selector
            
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
        
        menu_option = int(input("Choose movie activity to perform: "))
        
        return menu_option

            
    def text_resource_menu(self, user):
        text_menu_list =["Add text", "View text list", "Borrow text", "Return text", "Read text", "Purchase text", "Donate text"]
        if user == "admin":
            text_menu = text_menu_list
            for i in range(len(text_menu)):
                print(f"{i+1}. {text_menu[i]}")
        elif user != "admin":
            text_menu = text_menu_list[1:]
            for i in range(len(text_menu)):
                print(f"{i+1}. {text_menu[i]}")
                
        menu_option = int(input('Select what you want to do with text: '))
        
        return menu_option
            
    
    def event_resource_menu(self, user):
        pass

    def buy_purchase(self, resource_type):
        return super().buy_purchase(resource_type)
    
    def borrow_lease(self, resource_type):
        return super().borrow_lease(resource_type)
    
    def return_resource(self, resource_type):
        return super().return_resource(resource_type)