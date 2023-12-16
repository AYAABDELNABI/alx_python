"""
A module that has a class named base which will be 
the “base” of all other classes in this project. 
The goal of it is to manage id attribute in all your future classes and 
to avoid duplicating the same code 
"""

class Base:
    """
    A class that have:
    - Private attribute 
    - class constructor
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        A class constructor with argument id
        """
        if id is not None:
            self.id = id 
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects 