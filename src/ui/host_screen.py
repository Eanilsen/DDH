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

        # CanvasLayout is a subclass of BoxLayout that adds a black background
        self.canvas_layout = CanvasLayout()
        self.add_widget(self.canvas_layout)

        # A label displaying the page name
        self.label_host_game = Label(text="Host a Game!",
                                     font_size=40,
                                     size_hint=(.25, .10),
                                     pos_hint={'center_x': .5, 'center_y': .8})
        self.canvas_layout.add_widget(self.label_host_game)

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

        # Container to add Server Name and Max Players on the same line
        self.ui_container = BoxLayout(orientation='horizontal',
                                      size_hint=(.4, .2),
                                      pos_hint={'center_x': .5, 'center_y': .5})

        self.ui_container.add_widget(self.server_name_input)
        self.ui_container.add_widget(self.max_players_input)
        self.canvas_layout.add_widget(self.ui_container)

        self.description_input = TextInput(hint_text='Description',
                                           focus=False,
                                           size_hint=(.4, .1),
                                           pos_hint={'center_x': .5, 'center_y': .5},
                                           multiline=True)

        self.canvas_layout.add_widget(self.description_input)

        # The button to start a game
        self.start_game_button = Button(text='Start Game',
                                        size_hint=(.4, .05),
                                        pos_hint={'center_x': .5, 'center_y': .5})
        self.canvas_layout.add_widget(self.start_game_button)

class CanvasLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(CanvasLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (.8, .8)
        self.padding = (0, 0, 0, 100)
        self.pos_hint = {'center_x': .5, 'center_y': .5}
        self.spacing = 5

        canvas = self.canvas
        with canvas:
            Color(0, 0, 0, .5)  # Black with 50 Opacity (RBGA)
            self.rect = Rectangle(pos=self.center,
                                  size=(self.width / 2, self.height / 2))

        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
