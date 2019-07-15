from kivy.uix.textinput import TextInput
import re

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
