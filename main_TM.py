from kivy.config import Config
Config.set('kivy','keyboard_mode','systemanddock')
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime


"""
First class to open dialogue box where user inputs task

__init__ is an OOP method, called everytime an object is created from a class,
    lets the class intialize object's attributes.
    uses keyword self to assign the values passed as arguments to the objects attributes. 
    class Dog:
    def __init__(self, dogBreed, dogEyeColour):    
        self.breed = dog.Breed
        self.eyecolour = dog.EyeColour  # now creating an object
tomita = Dog("fox terrier","brown")

"""
class DialogContent(MDBoxLayout):
    def __init__(self):


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = ("Orange")



if __name__ == "__main":
    app = MainApp()
    app.run()