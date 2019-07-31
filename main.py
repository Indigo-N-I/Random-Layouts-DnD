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
from Items import OpenSpace, Blank
import adjustSize as adj

class OptionsScreen(GridLayout):

    def __init__(self, **kwargs):
        super(OptionsScreen, self).__init__(**kwargs)
        self.enter = rand.whereEnter()

# self.ids.layout.remove_widget(self.ids.counts)
    #adds an openspace tile
    def OpenSpace(self):
        self.add_widget(OpenSpace(self.cols, self.rows, size_hint_x=1, size_hint_y = 1, width=50, height = 50))

    #adds in a wall
    def Wall(self):
        self.add_widget(Blank(self.cols, self.rows, size_hint_x=1, size_hint_y = 1, width=50, height = 50))

    #used for top and bottom to add enterence
    def TopBot(self, y, gap, x):
        for i in range(y):
            enterLeft = x
            for i in range(self.cols):
                if i < gap:
                    self.Wall()
                elif enterLeft > 0:
                    self.OpenSpace()
                    enterLeft -=1
                else:
                    self.Wall()

    def completeFill(self, num):
        for i in range(num):
            self.OpenSpace()

    #Creates the board
    def fill(self, inX, inY):
        #if it is just a box
        def gapRow():
            for j in range(self.cols):
                if j< (self.cols - inX if self.enter == 2 else inX):
                    self.OpenSpace()
                else:
                    self.Wall()
        if inX == inY == 0:
            for i in range(self.cols * self.rows):
                self.OpenSpace()

        #if enterence on top
        if self.enter == 1:
            gap = rand.gap(self.cols, inX)
            self.TopBot(inY, gap, inX)
            self.completeFill(self.cols * (self.rows-inY))

        #if enternce on bottom
        #if enterence on bottom
        elif self.enter == 3:
            gap = rand.gap(self.cols, inX)
            self.completeFill(self.cols * (self.rows-inY))
            self.TopBot(inY, gap, inX)
        #if enterence on the right
        elif self.enter == 2:
            gap = rand.gap(self.rows, inY)
            for i in range(gap):
                gapRow()
            self.completeFill(inY* self.cols)
            for i in range(self.rows - gap - inY):
                gapRow()
        #if enterence is on the left
        elif self.enter == 4:
            gap = rand.gap(self.rows, inY)
            for i in range(gap):
                gapRow()
            self.completeFill(inY* self.cols)
            for i in range(self.rows - gap - inY):
                gapRow()

    def update(self):
        try:
            x, y, enterX, enterY = rand.getDimentions(self.defSize.text)
            print(x,y, enterX, enterY)
            self.createSize(x, y, enterX, enterY)
            self._fill_rows_cols_sizes()
            self._trigger_layout()
            self.clear_widgets()
            #pprint(vars(self))
            self.fill(enterX, enterY)
            adj.changeSize(self.cols, self.rows)
        except Exception as e:
            print(e)

    def createSize(this, x, y, enterX, enterY):
        this.col_default_width = 15
        this.row_default_height = 15
        print('creating room')
        if(this.enter == 1 or this.enter == 3):
            this.cols = x
            this.rows = y + enterY
        else:
            this.cols = x + enterX
            this.rows = y
        this._fill_rows_cols_sizes()


class DNDRandomizerApp(App):

    def build(self):
        return OptionsScreen(cols = 2, rows = 3)


if __name__ == '__main__':
    DNDRandomizerApp().run()
