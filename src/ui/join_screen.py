"""
Join Screen that players will interact with when browsing and selecting
games to join
"""

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from src.util import filehandler
  
class JoinScreen(Screen):
    """
    Implementation of the join screen
    """
    def __init__(self, **kwargs):
        super(JoinScreen, self).__init__(**kwargs)
        self.confirm_button = None
        self.background = Image(
            source='src/images/background.jpg',
            allow_stretch=True,
            keep_ratio=False)
        self.add_widget(self.background)

        self.join_label = Label(
            font_name='src/fonts/BLKCHCRY.TTF',
            text='Join Game',
            font_size='40sp',
            size_hint=(.8, .5),
            pos_hint={'center_x': .5, 'center_y': .7})

        self.enter_game_input = TextInput(
            hint_text='Enter address of host',
            multiline=False,
            size_hint=(.25, .1),
            pos_hint={'center_x': .5, 'center_y' : .525})
        self.join_button = Button(
            text='Join',
            size_hint=(.2, .1),
            pos_hint={'center_x': .5, 'center_y': .4})

        self.load_button = Button(text='Load .ddh file',
                                  size_hint=(.2, .05),
                                  pos_hint={'center_x': .5, 'center_y': .3})

        self.load_button.bind(on_release=self.show_load)

        self.float_layout = FloatLayout()
        self.float_layout.add_widget(self.join_label)
        self.float_layout.add_widget(self.enter_game_input)
        self.float_layout.add_widget(self.join_button)
        self.float_layout.add_widget(self.load_button)
        self.add_widget(self.float_layout)

        self.back_button = Button(
            font_name='src/fonts/Enchanted_Land.otf',
            text='Back', 
            font_size=24,
            size_hint=(.10, .05), 
            pos_hint={'center_x' : .95, 'bottom_y' : .025})
        self.add_widget(self.back_button)

    def show_load(self, *args):
        file_handler = filehandler.FileHandler()
        file_handler.show_load_popup()
