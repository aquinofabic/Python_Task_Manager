# from kivy.config import Config
# Config.set('kivy','keyboard_mode','systemanddock')
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime

# First class to open dialogue box where user inputs task
class DialogContent(MDBoxLayout):
    # the init function for class constructer
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = datetime.now().strftime("%A %d %B %Y")
        # set self.id's. date's text. text property inside date_text = ...
        # strftime is string format time

    # This function will show the date picker
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save = self.on_save)

    # This function will get date and save in a friendly form
    def on_save(self, instance, value, date_range):
        date = value.strftime("%A %d %B %Y")
        self.ids.date_text.text = str(date)

# Add main App class
class MainApp(MDApp):
    # Flag for show_task_function
    task_list_dialog = None
    # This is the build function for setting theme
    def build(self):
        self.theme_cls.primary_palette = ("Orange")

    # This is the show task function
    def show_task_dialog(self):
        if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
                title = "Create Task",
                type = "custom",
                content_cls = DialogContent()
            )
            self.task_list_dialog.open()

    # Add tasks
    def add_task(self, task, task_date):
        print(task.text, task_date)

    # Dialog closing function
    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()


if __name__ == "__main__":
    app = MainApp()
    app.run()


# 31.02s