"""
A module that have an empty class with override to dir() method
"""

class MetaClass(type):
    """
    Override dir() method to execlude __init__subclass__
    """
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']


class BaseGeometry(metaclass=MetaClass):
    """
    BaseGeometry class that uses the overriden dir() method 
    """
    
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
    def area(self):
        """
        A public method that raise an exception
        """
        raise Exception ("area() is not implemented")
    def integer_validator(self, name, value):
        """
        A public method that validates value:
        - If value is not an integer: raise a TypeError exception, 
          with the message <name> must be an integer
        - If value is less or equal to 0: raise a ValueError exception with the 
         message <name> must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        
BaseGeometry = __import__('5-base_geometry').BaseGeometry

        
class Rectangle(BaseGeometry):
    """
    A class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiate with width and height
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)