from kivy.uix.widget import Widget
from kivy.uix.image import Image

class OpenSpace(Image):
    def __init__(self, **kargs):

        super(OpenSpace, self).__init__(**kargs, source = 'tile.png')
