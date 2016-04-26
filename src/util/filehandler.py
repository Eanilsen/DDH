import kivy
kivy.require('1.9.1')

try:
    import cPickle as pickle
except:
    import pickle

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

import os

Builder.load_string("""
<File_Handler>:
    id: file_handler
    Button:
        text: "open"
        on_release: file_handler.load(filechooser.path, filechooser.selection)
    FileChooserIconView:
        id: filechooser
        on_selection: file_handler.selected(filechooser.selection)
""")

class File_Handler(BoxLayout):
    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as f:
            print self.deserialize(f.read())

    def selected(self, filename):
        print "selected: %s" % filename[0]

    def deserialize(self, filename):
        return pickle.loads(filename)


class MyApp(App):
    def build(self):
        return File_Handler()

if __name__ == '__main__':
    MyApp().run()
