import os
import re
import platform
try:
    import cPickle as pickle
except:
    import pickle

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.textinput import TextInput
import kivy
kivy.require('1.9.1')

class FileHandler(BoxLayout):
    def __init__(self, **kwargs):
        super(FileHandler, self).__init__(**kwargs)

        load_btn = Button(text='Load')
        load_btn.bind(on_release=self.show_load_popup)
        self.add_widget(load_btn)

        save_btn = Button(text='Save')
        save_btn.bind(on_release=self.show_save_popup)
        self.add_widget(save_btn)

        self.test = ["aoeu", 1]


    def show_load_popup(self, *args):
        load_btn = Button(text='Load', size_hint=(.08, .05))
        file_chooser = FileChooserIconView(path="../../saves")

        content = FloatLayout()
        content.clear_widgets()
        content.add_widget(file_chooser)
        content.add_widget(load_btn)

        popup = Popup(title="Load a file", content=content)
        load_callback = lambda load: self.load(
            file_chooser.path,
            file_chooser.selection, popup)
        load_btn.bind(on_release=load_callback)
        popup.open()

    def show_save_popup(self, *args):
        text_input = TextInput(
            size_hint=(.20, .05),
            pos_hint={'center_x': .5, 'bottom_y': .05})
        save_btn = Button(text='Save', size_hint=(.08, .05))
        file_chooser = FileChooserIconView(path="../../saves")

        content = FloatLayout()
        content.clear_widgets()
        content.add_widget(file_chooser)
        content.add_widget(save_btn)
        content.add_widget(text_input)

        popup = Popup(title="Save a file", content=content)

        serialize_callback = lambda save: self.serialize(
            file_chooser.path, text_input.text, popup)
        save_btn.bind(on_release=serialize_callback)

        popup.open()

    def load(self, path, filename, popup):
        if platform.system() == "Linux":
            try:
                file_name = filename[0]
                file_index = [m.start() for m in re.finditer('/', file_name)]
                with open(os.path.join(path, file_name[file_index[-1]+1:]),
                        'rb')as in_file:
                    print self.deserialize(in_file.read())
            except:
                print "nope"
        elif platform.system() == "Windows":
            try:
                file_name = filename[0]
                file_index = [m.start() for m in re.finditer('\\', file_name)]
                with open(os.path.join(path, file_name[file_index[-1]+1:]),
                        'rb')as in_file:
                    print self.deserialize(in_file.read())
            except:
                print "nope"
        popup.dismiss()

    def deserialize(self, file_string):
        return pickle.loads(file_string)

    def serialize(self, path, out_file, popup):
        with open(os.path.join(path, out_file + '.ddh'), 'wb') as of:
            pickle.dump(self.test, of)
        popup.dismiss()

class MyApp(App):
    def build(self):
        return FileHandler()

if __name__ == '__main__':
    MyApp().run()