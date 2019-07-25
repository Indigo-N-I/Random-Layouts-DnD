from kivy.uix.widget import Widget
from kivy.uix.image import Image

class OpenSpace(Image):
    def __init__(self,x, y, **kargs):

        super(OpenSpace, self).__init__(**kargs, source = 'tile.jpg', allow_stretch = False)

class Blank(Image):
    def __init__(self,x, y, **kargs):

        super(Blank, self).__init__(**kargs, source = 'blackImage.jpg', allow_stretch = True)
