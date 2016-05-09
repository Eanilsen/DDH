from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.graphics import *


class HostScreen(Screen):
    def __init__(self, **kwargs):
        super(HostScreen, self).__init__(**kwargs)
        self.background = Image(source='images/background.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)
        with self.canvas:
            Color(0, 0, 0, .5)  # Black with 50 Opacity (RBGA)
            Rectangle(pos=self.pos, size=self.size)

        # Back Button
        self.back_button = Button(text='Back', size_hint=(.10, .05), pos_hint={'center_x': .95, 'bottom_y': .025})
        self.add_widget(self.back_button)

        # The Box containing text inputs and a button to start game
        self.box_layout = BoxLayout(orientation='vertical', size_hint=(.8, .8), padding=(0, 0, 0, 100),
                                    pos_hint={'center_x': .5, 'center_y': .5}, spacing=5)
        self.add_widget(self.box_layout)

        # A label displaying the page name
        self.label_server_settings = Label(text="Server Settings", font_size=50, size_hint=(.25, .10),
                                           pos_hint={'center_x': .5, 'center_y': .70})
        self.box_layout.add_widget(self.label_server_settings)

        # Text input for the server name
        self.server_name_input = TextInput(hint_text='Server Name', focus=False, size_hint=(.4, .02),
                                           pos_hint={'center_x': .5, 'center_y': .5}, multiline= False)
        self.box_layout.add_widget(self.server_name_input)

        # Text input for the maximum players, taking only int as a value
        self.max_players_input = TextInput(hint_text='Number of Maximum Players', focus=False, size_hint=(.4, .02),
                                           input_filter='int', pos_hint={'center_x': .5, 'center_y': .5}, multiline=False)
        self.box_layout.add_widget(self.max_players_input)

        # The button to start a game
        self.host_game_button = Button(text='Start Game', size_hint=(.4, .015),
                                       pos_hint={'center_x': .5, 'center_y': .5})
        self.box_layout.add_widget(self.host_game_button)



