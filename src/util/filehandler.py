from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.button import Button

import os
import cPickle as pickle
import kivy
kivy.require('1.9.1')

pikk_kukk = []

def show_chooser(self):
    pikk_kukk.append(FileChooserIconView(path='../../saves'))
    return pikk_kukk[0]

def show_popup(self):
    content = FloatLayout()
    content.add_widget(show_chooser(self))
    popup = Popup(title='Load file', content=content)
    popup.open()

save_btn = Button(text='Save')
open_btn = Button(text='Open')
open_btn.bind(on_release=show_popup)

class MyApp(App):
    def build(self):
        layout = BoxLayout()
        layout.add_widget(open_btn)
        return layout


# def load(self, path, filename):
#     with open(os.path.join(path, filename[0]), 'rb') as f:
#         print self.deserialize(f.read())

# def deserialize(self, file_string):
#     return pickle.loads(file_string)

# def serialize(self, path, out_file):
#     with open(os.path.join(path, out_file + '.ddh'), 'wb') as of:
#         pickle.dump(self.test, of)

if __name__ == '__main__':
    MyApp().run()
