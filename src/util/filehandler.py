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

    def load(self, path, filename):
        file_name = filename[0]
        file_index = [m.start() for m in re.finditer('/', file_name)]
        with open(os.path.join(path, file_name[file_index[-1]+1:]),
                  'rb')as in_file:
            print self.deserialize(in_file.read())

    def deserialize(self, file_string):
        return pickle.loads(file_string)


class SaveLayout(BoxLayout):

    test = ["aoeu", 1]

    def serialize(self, path, out_file):
        with open(os.path.join(path, out_file + '.ddh'), 'wb') as of:
            pickle.dump(self.test, of)


def show_save_popup(self):
    sl = SaveLayout()
    content = BoxLayout()
    content.add_widget(sl)
    popup = Popup(title="Save file", content=content)
    popup.open()

def show_load_popup(self):
    ll = LoadLayout()
    content = FloatLayout()
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
