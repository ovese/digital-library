from resources import Resources
import os
# time
import time
# datetime and date
from datetime import datetime, date

global DATETIME_STRING_FORMAT
DATETIME_STRING_FORMAT = "%Y-%m-%d"  # this should be global

class Texts(Resources):
    def __init__(self, resource_name_title, resource_owner, resource_description, resource_type) -> None:
        super().__init__(resource_name_title, resource_owner, resource_description, resource_type)
        
    def add_text(self, text_type):
        """Depending on the text type param, the entered text will be placed in the
        right storage file:
        I am going to decide what type of file this should be. It could be a 
        simple text file or a database sql file"""
        if not os.path.exists("text_resource_file.txt"):
            with open("text_resource_file.txt", "w") as all_text_type_file:
                # default all_text_type_file.txt entry has the format
                # Text author;Text title;Text type;Text description;Publish date;available
                all_text_type_file.write("Text author;Text title;Text type;Text description;Publish date;available")

            with open("all_text_type_file.txt", 'r') as text_file_to_read:
                text_data = text_file_to_read.read().split("\n")
                text_data = [t for t in text_data if t != ""]  # list comprehension used here
                
                task_list = []  # I have used this so much, I should make it global/ class variable
                for t_str in text_data:
                    curr_text_data = {}

                    # Split by semicolon and manually add each component
                    # I am adding the task ID data field here to allow the task.txt
                    # have a serial number or task_ID entry
                    text_components = t_str.split(";")
                    # curr_t['task_id'] = task_components[0]
                    curr_text_data['text_author'] = text_components[0]
                    curr_text_data['text_title'] = text_components[1]
                    curr_text_data['text_type'] = text_components[2]
                    curr_text_data['text_description'] = text_components[3]
                    curr_text_data['publish_date'] = datetime.strptime(text_components[4], DATETIME_STRING_FORMAT)
                    curr_text_data['borrowed'] = True if text_components[5] == "Yes" else False
                    task_list.append(curr_text_data)