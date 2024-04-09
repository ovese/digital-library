from text_resource import Texts

class Books(Texts):
    def __init__(self, resource_name_title, resource_owner, resource_description, resource_type) -> None:
        super().__init__(resource_name_title, resource_owner, resource_description, resource_type)