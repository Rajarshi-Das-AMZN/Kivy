import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


# GridLayout Making
class XavartzGrid(GridLayout):              # GridLayout Widget Making
    def __init__(self, **kwargs):
        super(XavartzGrid, self).__init__()         # constructor invoked
        self.cols = 2                               # Column Numbers
        self.add_widget(Label(text="Student Name: "))

        self.s_name = TextInput()           # we can give TextInput(multiline=False)
        self.add_widget(self.s_name)

        self.add_widget(Label(text="Student Marks: "))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text="Student Gender: "))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.press = Button(text="Submit")
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):
        print("Name of the student is: "+self.s_name.text)
        print("Marks of student is: "+self.s_marks.text)
        print("Gender is: "+self.s_gender.text)


# Main App Making
class XavartzApp(App):
    def build(self):
        return XavartzGrid()


if __name__ == "__main__":
    XavartzApp().run()