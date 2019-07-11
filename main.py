from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
import re
import buttonFunct as bf
import randomizer as rand

class IntInput(TextInput):

    pat = re.compile('[0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if pat.match(substring):
            return super(IntInput, self).insert_text(substring, from_undo = from_undo)
        else:
            return super(IntInput, self).insert_text('', from_undo = from_undo)


class SizeInput(TextInput):

    def insert_text(self, substring, from_undo=False):
        if len(self.text) == 1:
            return super(SizeInput, self).insert_text('', from_undo = from_undo)
        elif (substring == 'S' or substring == 'M' or substring == 'L'):
            return super(SizeInput, self).insert_text(substring, from_undo = from_undo)
        else:
            return super(SizeInput, self).insert_text('', from_undo = from_undo)


class OptionsScreen(Widget):

    # def __init__(self, **kwargs):
    #     super(OptionsScreen, self).__init__(**kwargs)
    #     self.cols = 2
    #     self.add_widget(Label(text='Size of Map (S, M, L)'))
    #     self.defSize = SizeInput()
    #     self.add_widget(self.defSize)
    #     self.add_widget(Label(text='Number of Counters'))
    #     self.counters = IntInput()
    #     self.add_widget(self.counters)


    def update(self):
        try:
            x, y, enterX, enterY = rand.getDimentions(self.defSize.text)
            print(x,y, enterX, enterY)
        except Exception as e:
            print(e)




class MyApp(App):

    def build(self):
        return OptionsScreen()


if __name__ == '__main__':
    MyApp().run()
