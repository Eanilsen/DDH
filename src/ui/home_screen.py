from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.background = Image(
            source='images/background.jpg',
            allow_stretch=True,
            keep_ratio=False)
        self.add_widget(self.background)

        self.label = Label(text='Welcome to DDH!',
            font_size='20sp', size_hint=(.25, .10),
            pos_hint={'center_x' : .5, 'center_y' : .70})
        self.add_widget(self.label)

        self.buttons = BoxLayout(size_hint=(.25, .15),
            pos_hint={'center_x' : .5, 'center_y' : .5})
        self.buttons.spacing = 5;
        self.buttons.orientation = 'vertical'

        self.join_button = Button(text='Join')
        self.buttons.add_widget(self.join_button)

        self.host_button = Button(text='Host')
        self.buttons.add_widget(self.host_button)

        self.character_button = Button(text='Characters')
        self.buttons.add_widget(self.character_button)

        self.add_widget(self.buttons)

        self.quit_button = Button(
            text='Quit', size_hint=(.10, .05),
            pos_hint={'center_x' : .95, 'bottom_y' : .025})
        self.add_widget(self.quit_button)
