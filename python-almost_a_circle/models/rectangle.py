"""
A module related to Python Almost a circle project 
that has a class Rectangle that inherits from Base 
- Has private attributes: __width , __height , __x , __y 
- Class constructor: 

"""
from models.base import Base

class Rectangle(Base):
    """
    A class Rectangle that inherits from Base
    private instanve attriubtes:
    1- width
    3- height
    4- x
    5- y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        A constructor method to instatiate instances with arguments 
        Validates arguments accordingly 
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.validate_width()
        self.validate_height()
        self.validate_x()
        self.validate_y()

    def validate_width(self):
        """
        A method that validates width
        """
        if not isinstance(self.__width,int):
            raise TypeError("width must be an integer")
        elif self.__width <= 0:
            raise ValueError("width must be > 0")
    
    def validate_height(self):
        """
        A method that validates height
        """
        if not isinstance(self.__height,int):
            raise TypeError("height must be an integer")
        elif self.__height <= 0:
            raise ValueError("height must be > 0")
    
    def validate_x(self):
        """
        A method that validates x
        """
        if not isinstance(self.__x,int):
            raise TypeError("x must be an integer")
        elif self.__x < 0:
            raise ValueError("x must be >= 0")
    
    def validate_y(self):
        """
        A method that validates y
        """
        if not isinstance(self.__y,int):
            raise TypeError("y must be an integer")
        elif self.__y < 0:
            raise ValueError("y must be >= 0")
    
    def area(self):
        """
        A method that returns the area of rectangle
        """
        return self.__height * self.__width
    
    def display(self):
        """Method that prints in stdout the rectangle with the character #"""
        for space in range(0,self.__y):
            print()
        for height in range(0,self.__height):
            for tab in range(0,self.__x):
                print(" ", end="")
            for width in range(0,self.__width):
                    
                 print("#", end="")
            print()
    def __str__(self):
        """
        A method that  overriding the __str__ method so that it returns 
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,self.__x,self.__y,self.__width,self.__height)
    def update(self, *args, **kwargs):
        """
        A method that assigns an argument to each attribute:

        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        for key,value in kwargs.items():
            if len(args) != 0:
                break
            elif key == 'id':
                self.id = value
            elif key == 'width':
                self.__width = value
            elif key == 'height':
                self.__height = value
            elif key == 'x':
                self.__x = value
            elif key == 'y':
                self.__y = value 

        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.__width = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
        elif len(args) == 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
    
        


    @property
    def width(self):
        """
        Width getter method
        """
        return self.__width
    @width.setter
    def width(self, width):
        """
        Width setter method
        Validates that the input is inteager and greater than zero
        """
        if not isinstance(width,int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
    @property
    def height(self):
        """
        Height getter method
        """
        return self.__height 
    @height.setter
    def height(self, height):
        """
        Height setter method
        Validates that the input is inteager and greater than zero
        """
        if not isinstance(height,int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        Attributet x getter method
        """
        return self.__x
    @x.setter
    def x(self, x):
        """
        Attribute x setter method
        Validates that the input is inteager and greater than or equals zero
        """
        if not isinstance(x,int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
    @property
    def y(self):
        """
        Attribute y getter method
        """
        return self.__y
    @y.setter
    def y(self, y):
        """
        Attribute y setter method
        Validates that the input is inteager and greater than or equals zero
        """
        if not isinstance(y,int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y



    