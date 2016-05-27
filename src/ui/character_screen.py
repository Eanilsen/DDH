from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput

class CharacterScreen(Screen):
    def __init__(self, **kwargs):
        super(CharacterScreen, self).__init__(**kwargs)
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        self.background = Image(
            source='images/background.jpg',
            allow_stretch=True,
            keep_ratio=False)
        self.layout.add_widget(self.background)

        self.create_layouts()
        self.add_labels()
        self.add_textfields()
        self.add_buttons()

    def create_layouts(self):
        self.buttons = BoxLayout(
            orientation='vertical',
            spacing=15, 
            pos_hint={'center_x': .25, 'center_y': .5},
            size_hint=(.5, .5))

        self.labels = BoxLayout(
            orientation='vertical',
            spacing=20,
            pos_hint={'center_x': .35, 'center_y': .85},
            size_hint=(.5, .22))

        self.txt_inputs = BoxLayout(
            orientation='vertical',
            spacing=20,
            pos_hint={'center_x': .9, 'center_y': .85},
            size_hint=(.5, .22))

        self.layout.add_widget(self.buttons)
        self.layout.add_widget(self.labels)
        self.layout.add_widget(self.txt_inputs)

    def add_labels(self):
        self.name_label = Label(
            text='Name',
            font_size=24)

        self.class_label = Label(
            text='Class',
            font_size=24)

        self.hp_label = Label(
            text='HP',
            font_size=24)

        self.labels.add_widget(self.name_label)
        self.labels.add_widget(self.class_label)
        self.labels.add_widget(self.hp_label)

    def add_textfields(self):
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

    def add_buttons(self):
        self.new_button = Button(
            text='New',
            size_hint=(.30, .15))

        self.save_button = Button(
            text='Save',
            size_hint=(.30, .15))

        self.load_button = Button(
            text='Load',
            size_hint=(.30, .15))

        self.join_button = Button(
            text='Join',
            size_hint=(.30, .15))

        self.back_button = Button(
            text='Back',
            size_hint=(.10, .05),
            pos_hint={'center_x': .95, 'bottom_y': .025})

        self.buttons.add_widget(self.new_button)
        self.buttons.add_widget(self.save_button)
        self.buttons.add_widget(self.load_button)
        self.buttons.add_widget(self.join_button)
        self.layout.add_widget(self.back_button)
