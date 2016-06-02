from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from src.util import filehandler

class CharacterScreen(Screen):
    def __init__(self, **kwargs):
        super(CharacterScreen, self).__init__(**kwargs)

        self.layout = FloatLayout()
        self.add_widget(self.layout)

        self.background = Image(
            source='src/images/background.jpg',
            allow_stretch=True,
            keep_ratio=False)
        self.layout.add_widget(self.background)

        self.buttons = BoxLayout(
            orientation='vertical',
            spacing=15, 
            pos_hint={'center_x': .25, 'center_y': .5},
            size_hint=(.5, .30))
        self.layout.add_widget(self.buttons)

        self.new_button = Button(
            font_name='src/fonts/Enchanted_Land.otf',
            text='New',
            size_hint=(.30, .15),
            font_size=24)

        self.save_button = Button(
            font_name='src/fonts/Enchanted_Land.otf',
            text='Save',
            size_hint=(.30, .15),
            font_size=24)

        self.load_button = Button(
            font_name='src/fonts/Enchanted_Land.otf',
            text='Load',
            size_hint=(.30, .15),
            font_size=24)

        self.join_button = Button(
            font_name='src/fonts/Enchanted_Land.otf',
            text='Join',
            size_hint=(.30, .15),
            font_size=24)

        self.buttons.add_widget(self.new_button)
        self.buttons.add_widget(self.save_button)
        self.buttons.add_widget(self.load_button)
        self.buttons.add_widget(self.join_button)

        self.labels = BoxLayout(
            orientation='vertical',
            spacing=20,
            pos_hint={'center_x': .35, 'center_y': .85},
            size_hint=(.5, .22))

        self.name_label = Label(
            font_name='src/fonts/Enchanted_Land.otf',
            text='Name',
            font_size=35)

        self.class_label = Label(
            font_name='src/fonts/Enchanted_Land.otf',
            text='Class',
            font_size=35)

        self.hp_label = Label(
            font_name='src/fonts/Enchanted_Land.otf',
            text='HP',
            font_size=35)

        self.labels.add_widget(self.name_label)
        self.labels.add_widget(self.class_label)
        self.labels.add_widget(self.hp_label)

        self.layout.add_widget(self.labels)

        self.txt_inputs = BoxLayout(
            orientation='vertical',
            spacing=20,
            pos_hint={'center_x': .9, 'center_y': .85},
            size_hint=(.5, .22))

        self.name_input = TextInput(
            hint_text='Enter name',
            size_hint=(.6, .15))

        self.class_input = TextInput(
            hint_text='Enter Class',
            size_hint=(.6, .15))

        self.hp_input = TextInput(
            hint_text='Enter HP',
            size_hint=(.6, .15))

        self.txt_inputs.add_widget(self.name_input)
        self.txt_inputs.add_widget(self.class_input)
        self.txt_inputs.add_widget(self.hp_input)

        self.layout.add_widget(self.txt_inputs)

        self.back_button = Button(
            font_name='src/fonts/Enchanted_Land.otf',
            text='Back',
            font_size=24,
            size_hint=(.10, .05),
            pos_hint={'center_x': .95, 'bottom_y': .025})
        self.layout.add_widget(self.back_button)

        # Save and load related code
        self.file_handler = filehandler.FileHandler()
        self.save_button.bind(on_release=self.save)
        self.load_button.bind(on_release=self.file_handler.show_load_popup)

    def save(self, *args):
        file_handler = filehandler.FileHandler()
        save_unit_list = self.make_serializable()
        file_handler.show_save_popup(save_unit_list)

    def make_serializable(self):
        serializable_list = []
        serializable_list.append(self.name_input.text)
        serializable_list.append(self.class_input.text)
        serializable_list.append(self.hp_input.text)
        return serializable_list

