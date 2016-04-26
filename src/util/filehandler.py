from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

import os
import cPickle as pickle
import kivy
kivy.require('1.9.1')

Builder.load_string("""
<File_Handler>:
    id: file_handler
    Button:
        text: "open"
        on_release: file_handler.load(filechooser.path, filechooser.selection)
    Button:
        text: "save"
        on_release: file_handler.serialize(filechooser.path, 'test')
    FileChooserIconView:
        id: filechooser
        path: "../../saves/"
""")

class File_Handler(BoxLayout):
    test = ['a','b','c',1,2,3]

    def load(self, path, filename):
        with open(os.path.join(path, filename[0]), 'rb') as f:
            print self.deserialize(f.read())

    def deserialize(self, file_string):
        return pickle.loads(file_string)

    def serialize(self, path, out_file):
        with open(os.path.join(path, out_file + '.ddh'), 'wb') as of:
            pickle.dump(self.test, of)


class MyApp(App):
    def build(self):
        return File_Handler()

if __name__ == '__main__':
    MyApp().run()
