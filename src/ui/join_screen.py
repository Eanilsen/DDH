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

class GameBox(BoxLayout):
    """
    Contains all the information about one specific game.
    One game == One instance of GameBox
    """
    def __init__(self, name, num_players, desc, **kwargs):
        super(GameBox, self).__init__(**kwargs)
        self.name = Label(text=name)
        self.players = Label(text=num_players)
        self.desc = Label(text=desc)

        self.add_widget(self.name)
        self.add_widget(self.players)
        self.add_widget(self.desc)

class GameOverView(BoxLayout):
    """
    Contains information about all avaialbe games via instances of gameboxes
    """
    def __init__(self, *games, **kwargs):
        super(GameOverView, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (.8, .5)
        self.pos_hint = {'center_x': .5, 'center_y': .5}
        for game in games:
            self.add_widget(game)

#pylint: disable=too-many-instance-attributes
class JoinScreen(Screen):
    """
    Implemntation of the join screen
    """
    def __init__(self, **kwargs):
        super(JoinScreen, self).__init__(**kwargs)

        self.background = Image(
            source='images/background.jpg',
            allow_stretch=True,
            keep_ratio=False)
        self.add_widget(self.background)

        self.float_layout = FloatLayout()
        self.add_widget(self.float_layout)
        #Sample game names, awaiting implemntation of dynamic entries until
        #we have a server-client setup running
        self.gbox = GameBox('Name', '0', 'Desc')
        self.gbox1 = GameBox('Name', '1', 'Desc')
        self.gbox2 = GameBox('Name', '2', 'Desc')
        self.gbox3 = GameBox('Name', '3', 'Desc')
        self.gbox4 = GameBox('Name', '4', 'Desc')
        self.gbox5 = GameBox('Name', '5', 'Desc')

        self.games = GameOverView(
            self.gbox, self.gbox1, self.gbox2, self.gbox3, self.gbox4,
            self.gbox5)

        self.float_layout.add_widget(self.games)

        self.buttons = BoxLayout(
            orientation='horizontal',
            size_hint=(.5, .1),
            pos_hint={'center_x': .5, 'center_y': .2})
        self.add_widget(self.buttons)

        self.join_button = Button(
            text='Join Game',
            pos_hint={'center_x': .5, 'center_y': .5})
        self.buttons.add_widget(self.join_button)
        self.filter_button = Button(
            text='Filter',
            pos_hint={'center_x': .5, 'center_y': .5})
        self.buttons.add_widget(self.filter_button)

        self.back_button = Button(
            text='Back', size_hint=(.10, .05),
            pos_hint={'center_x' : .95, 'bottom_y' : .025})
        self.add_widget(self.back_button)
