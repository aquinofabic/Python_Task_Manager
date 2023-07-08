"""""
PYTHON
__init__ is an OOP method, called everytime an object is created from a class,
    lets the class intialize object's attributes.
    uses keyword self to assign the values passed as arguments to the objects attributes.
    
    class Dog:
    def __init__(self, dogBreed, dogEyeColour):    
        self.breed = dog.Breed
        self.eyecolour = dog.EyeColour  # now creating an object
tomita = Dog("fox terrier","brown")
print("this dog is a" ,tomita.breed, "and eyes are", tomita.EyeColour)

___________________________________________________________________________________________

Unpacking operators: (*) is used to unpack iterables or argument lists, (**) is used to unpack dictionaries.

*args (for integers) and **kwargs (for keywords) allows you to pass multiple arguments/keyword arguments to a function. For example:
"""
def sum(a,b):
    return a + b  # limited to only two arguments
    

def arg_sum(*args):
    result = 0
    # Iterating over python args tuple
    for x in args:
        result += x
    return result
    
print(arg_sum(1,2,3))

"""
Note: args is just a name and * is the unpacking operator.
You are able to replace *args with, for example, *integers.

Note: the iterable object you'll get using the unpacking operator (*) is not a list, but a tuple! (lists [] are mutable, tuples () are not)
(**) can pass keyword arguments and returns both the key:value

___________________________________________________________________________________________

super() is an example of class inheritence.

markup modules provides unified interface for 

___________________________________________________________________________________________

KIVY
kivy's .bind(current = a_function(arg1, arg2)) method, when current property changes,
it will call a_function with arguments arg1, arg2

root function allows 

parent is a kivy property
"""""

