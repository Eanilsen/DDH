"""This module adds functionality for serializing(saving) and
deserializing(loading) of objects using the cPickle library.
"""
import os
import re
import cPickle as pickle

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.lang import Builder

import kivy
kivy.require('1.9.1')

Builder.load_string("""
<LoadLayout>:
    id: load_layout
    Button:
        text: "Load"
        size_hint: (.10, .05)
        pos_hint: {'center_x': 95, 'bottom_y': .025}
        on_release: load_layout.load(file_chooser.path, file_chooser.selection)
    FileChooserIconView:
        id: file_chooser
        path: "../../saves"

<SaveLayout>:
    id: save_layout
    TextInput:
        id: text_input
        size_hint: (.20, .05)
    Button:
        text: "Save"
        size_hint: (.05, .05)
        on_release: save_layout.serialize(file_chooser.path, text_input.text)
    FileChooserIconView:
        id: file_chooser
        path: "../../saves"
""")

class LoadLayout(BoxLayout):
    """The LoadLayout contains the filechooser and load button."""

    def load(self, path, filename):
        """Finds the filename based on the path by finding the last '/' and
        using whatever comes after as a filename.
        """
        file_name = filename[0]
        file_index = [m.start() for m in re.finditer('/', file_name)]
        with open(os.path.join(path, file_name[file_index[-1]+1:]),
                  'rb')as in_file:
            print self.deserialize(in_file.read())

    def deserialize(self, file_string):
        """Calls cPickle's load string function and returns the deserialized
        string.
        """
        return pickle.loads(file_string)


class SaveLayout(BoxLayout):
    """The SaveLayout contains the filechooser and save button."""

    test = ["aoeu", 1]

    def serialize(self, path, out_file):
        """Serializes an object and saves it to a out_file with the given path.
        """
        with open(os.path.join(path, out_file + '.ddh'), 'wb') as of:
            pickle.dump(self.test, of)


def show_save_popup(self):
    """Displays the SaveLayout as a popup contained in a BoxLayout."""
    sl = SaveLayout()
    content = BoxLayout()
    content.add_widget(sl)
    popup = Popup(title="Save file", content=content)
    popup.open()

def show_load_popup(self):
    """Displays the LoadLayout as a popup contained in a BoxLayout."""
    ll = LoadLayout()
    content = BoxLayout()
    content.add_widget(ll)
    popup = Popup(title='Load file', content=content)
    popup.open()

load_btn = Button(text='Load')
save_btn = Button(text='Save')
save_btn.bind(on_release=show_save_popup)
load_btn.bind(on_release=show_load_popup)


class MyApp(App):
    def build(self):
        layout = BoxLayout()
        layout.add_widget(load_btn)
        layout.add_widget(save_btn)
        return layout


if __name__ == '__main__':
    MyApp().run()
