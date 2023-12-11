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
        raise Exception ("area() is not implemented")