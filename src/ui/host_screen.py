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
        self.background = Image(source='images/background.jpg',
                                allow_stretch=True,
                                keep_ratio=False)
        self.add_widget(self.background)

        # Back Button
        self.back_button = Button(text='Back',
                                  size_hint=(.10, .05),
                                  pos_hint={'center_x': .95, 'bottom_y': .025})
        self.add_widget(self.back_button)

        # The Box containing text inputs and a button to start game
        self.box_layout = BoxLayout(orientation='vertical',
                                    size_hint=(1.2, .8),
                                    padding=(0, 0, 0, 100),
                                    pos_hint={'center_x': .5, 'center_y': .5},
                                    spacing=5)
        """
            https://kivy.org/docs/guide/graphics.html

            In .kv files I was able to add the Canvas to the box_layout defined further down. Now, with .py files,
            I can't do it anymore. When I use 'with self.canvas' I'm applying the canvas to the 'self', not the box_layout.

            I need a class or something (see kivy link) to make the canvas apply on the box layout and not take the whole
            screen.
        """
        with self.canvas:
            Color(0, 0, 0, .5)  # Black with 50 Opacity (RBGA)
            self.rect = Rectangle(pos=self.center,
                                  size=(self.width, self.height / 2))
        print self.rect.size
        self.bind(pos=self.update_rect,
                  size=self.update_rect)
        self.add_widget(self.box_layout)

        # A label displaying the page name
        self.label_server_settings = Label(text="Host a Game!",
                                           font_size=40,
                                           size_hint=(.25, .10),
                                           pos_hint={'center_x': .5, 'center_y': .75})
        self.box_layout.add_widget(self.label_server_settings)

        # Text input for the server name
        self.server_name_input = TextInput(hint_text='Server Name',
                                           size_hint=(.3, .25),
                                           focus=False,
                                           multiline=False)

        # Text input for the maximum players, taking only int as a value
        self.max_players_input = TextInput(hint_text='Max Players',
                                           size_hint=(.1, .25),
                                           focus=False,
                                           input_filter='int',
                                           multiline=False)

        self.ui_container = BoxLayout(orientation='horizontal',
                                      size_hint=(.4, .2),
                                      pos_hint={'center_x': .5, 'center_y': .5})

        self.ui_container.add_widget(self.server_name_input)
        self.ui_container.add_widget(self.max_players_input)
        self.box_layout.add_widget(self.ui_container)

        self.description_input = TextInput(hint_text='Description',
                                           focus=False,
                                           size_hint=(.4, .1),
                                           pos_hint={'center_x': .5, 'center_y': .5},
                                           multiline=True)

        self.box_layout.add_widget(self.description_input)

        # The button to start a game
        self.host_game_button = Button(text='Start Game',
                                       size_hint=(.4, .05),
                                       pos_hint={'center_x': .5, 'center_y': .5})
        self.box_layout.add_widget(self.host_game_button)



