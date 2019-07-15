from kivy.app import App
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, BoundedNumericProperty
)
from kivy.vector import Vector
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
import buttonFunct as bf
import randomizer as rand
from inputs import IntInput, SizeInput
from pprint import pprint
from Items import OpenSpace

class OptionsScreen(GridLayout):

    def __init__(self, **kwargs):
        super(OptionsScreen, self).__init__(**kwargs)
    #     self.cols = 2
    #     self.add_widget(Label(text='Size of Map (S, M, L)'))
    #     self.defSize = SizeInput()
    #     self.add_widget(self.defSize)
    #     self.add_widget(Label(text='Number of Counters'))
    #     self.counters = IntInput()
    #     self.add_widget(self.counters)

# self.ids.layout.remove_widget(self.ids.counts)

    def update(self):
        try:
            x, y, enterX, enterY = rand.getDimentions(self.defSize.text)
            print(x,y, enterX, enterY)
            self.createSize(x, y, enterX, enterY)
            self._fill_rows_cols_sizes()
            self._trigger_layout()
            self.clear_widgets()
            #pprint(vars(self))
            self.add_widget(OpenSpace())
        except Exception as e:
            print(e)

    def createSize(this, x, y, enterX, enterY):
        enter = rand.whereEnter()
        this.col_default_width = 15
        this.row_default_height = 15
        print('creating room')
        if(enter == 1 or enter == 3):
            this.cols = x
            this.rows = y + enterY
        else:
            this.cols = x + enterX
            this.rows = y
        this._fill_rows_cols_sizes()
        #pprint(vars(this))


class DNDRandomizerApp(App):

    def build(self):
        return OptionsScreen(cols = 2, rows = 3)


if __name__ == '__main__':
    DNDRandomizerApp().run()
