import os
import datetime
from resources import Resources

class Films(Resources):
    def __init__(self, resource_name_title, resource_owner, resource_description, resource_type) -> None:
        """I have had issues with circular imports which has made me remove this version of constructor.
        I have also had to remove the refernce to inheritance in the definition of the class. 
        Previously, I was inheriting from Resources class. It can be seeen that I have commented out the 
        reference to the import on line 3"""
        super().__init__(resource_name_title, resource_owner, resource_description, resource_type)
        print("Inside Films class constructor")
    
    # def __init__(self):
    #     pass

    def add_films_to_list(self, user):
        """Allows admin to add movie to library movies resource list.
        Allows admin to see if movie already added"""
        movie_str = ""
        if user == "admin":
            if not os.path.exists("movies_list.txt"):
                #
                with open("movies_list.txt", "w") as file_movies_format:
                    # specifying the format of data to be written to file
                    line_data_format = f"movie_title, movie_director, movie_type, movie_synopsis, movie_debut, movie_duration\n"
                    file_movies_format.write(line_data_format)
            elif os.path.exists("movies_list.txt"):
                with open("movies_list.txt", "a") as file_movie_to_add:
                    #        
                    # request movie to register details
                    try:
                        movie_title = input("Enter the movie title to register into database: ")
                        movie_director = input("Enter movie director\'s name: ")
                        movie_type = input("Enter genre of movie(Action, documentary, romance, horror): ")
                        movie_synopsis = input("Give brief description of movie: ")
                        movie_premiered = input("Enter debut year(yyyy): ")
                        movie_duration = input("Enter movie viewing duration(hh:mm): ")
                        
                        movie_str = f"{movie_title},{movie_director},{movie_type},{movie_synopsis},{movie_premiered},{movie_duration}\n"
                        file_movie_to_add.write(movie_str)
                    except FileNotFoundError as fnfe:
                        print(fnfe)
                    else:
                        pass
                    finally:
                        movies_file_path = os.path.basename("movies_list.txt")
                        print(f"File {movies_file_path}, was written to successfully!!!")
        else:
            print("Non-admin user cannot add resource to library")

    def view_films_list(self):
        """Reads a file of available movies in library resource list.
        Allows user select a specific movie to view.
        Allows user change selection of movie"""
        if os.path.exists("movies_list.txt"):
            with open("movies_list.txt", "r") as file_movies_available:
                # specifying the format of data to be written to file
                file_movies_available.readlines()
                
                # show the file contents here or move out of with-open block
                print(type(file_movies_available))
                print(file_movies_available)
        
    def borrow_lease(self, resource_type):
        # search list of movies to know if requested movie is available
        
        
        return super().borrow_lease(resource_type)
    
    def return_resource(self, resource_type):
        
        return super().return_resource(resource_type)
    
    def watch_film(self):
        self.resource_name_title = "The Good, The Bad, and The Ugly"
        
    def buy_purchase(self, resource_type):
        return super().buy_purchase(resource_type)
    
    def donate_movie(self, movie_title):
        return movie_title
    
    # define and implement a main method here which uses all the functions above
    # or that holds the logic for how this class is accessed and works
    def movie_manager(self, films_menu_option, instance_user):
        if instance_user == "admin":            
            if films_menu_option == 1:
                self.add_films_to_list(instance_user)
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
        elif instance_user != "admin":
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