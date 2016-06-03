from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.graphics import *
from kivy.uix.gridlayout import GridLayout
from random import random

class GamePlayerScreen(Screen):
    outer_layout = GridLayout(rows=2)
    top_container = GridLayout(cols=2,
                               pos_hint={'center_x': .5, 'top_y': 0},
                               size_hint=(1, .1),
                               spacing=800)
    bottom_container = BoxLayout(orientation='horizontal',
                                 pos_hint={'center_x': .5, 'top_y': 0},
                                 spacing=50)  # Spacing between tabPanel and players
    back_button = Button(text="Back",
                         pos_hint={"right_x": .5, "top_y": .5},
                         size_hint=(.08, .03))
    target_character_box = BoxLayout(orientation='horizontal')

    def __init__(self, **kwargs):
        super(GamePlayerScreen, self).__init__(**kwargs)
        self.background = Image(source='src/images/background.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)
        self.bottom_container.add_widget(TabbedActivityContainer())
        self.bottom_container.add_widget(PlayersPanel(6))
        self.top_container.add_widget(Player("src/images/portrait1.gif", "Name", "Role", "0/1000", "0,100"))
        self.top_container.add_widget(self.target_character_box)
        self.outer_layout.add_widget(self.top_container)
        self.outer_layout.add_widget(self.bottom_container)
        self.add_widget(self.outer_layout)
        self.add_widget(self.back_button)

'''
    This is the tabbed container. Most of the information from Character Sheets
    are displayed in the different tabs. You can choose what you want to view at any time.
    for documentation: https://kivy.org/docs/api-kivy.uix.tabbedpanel.html
'''
class TabbedActivityContainer(TabbedPanel):
    def __init__(self, **kwargs):
        super(TabbedActivityContainer, self).__init__(**kwargs)

        self.tab_pos = 'top_mid'
        self.do_default_tab = False
        self.background_color = (0, 0, 0, .5)
        self.size_hint = (.8, .8)
        self.tab_width = 150

        self.tab2 = TabbedPanelItem(text='Useful Info')
        self.tab2.add_widget(Label(text='Add some useful information to display in tab 2'))

        self.tab3 = TabbedPanelItem(text='Character Traits')
        self.tab3.add_widget(Label(text='Add traits here'))

        self.tab4 = TabbedPanelItem(text='Add a tab!')

        # Properties for the tabs. Currently does nothing:
        self.tabbed_strip = TabbedPanelStrip(background_color=(0,0,0,.5))
        self.add_widget(self.tabbed_strip)

        self.add_widget(MagicTab())  # TODO Do this with the other tabs as well!
        self.add_widget(self.tab2)
        self.add_widget(self.tab3)

'''
    This is information about the tab that holds magic
'''
class MagicTab(TabbedPanelItem):
    def __init__(self, **kwargs):
        super(MagicTab, self).__init__(**kwargs)
        self.text = 'Magic'
        tab_magic_ui = StackLayout(orientation='tb-lr',
                                   minimum_width=3100,
                                   padding=(5, 5, 0, 0),
                                   spacing=1)
        spells = ["Fireball", "Healing Rain", "Taunt", "Holy Light", "Steady Shot",
                  "Might", "Strike", "Dance"]
        for i in range(0, len(spells)):
            spell_string = spells[i]
            tab_magic_ui.add_widget(Button(text=spell_string,
                                           size_hint=(.2, .1)))  # Width of the buttons
        self.add_widget(tab_magic_ui)

'''
    PlayersPanel use the Player class to add as many players as there are names in the array
    player_names. I suggest that names are taken from character sheet and added there, or something
    similar.
'''
class PlayersPanel(BoxLayout):
    def __init__(self, player_amount, **kwargs):
        super(PlayersPanel, self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.spacing = 30
        self.size_hint = (.2, .75)  # Will stop at the size of TabbedActivityContainer()
        self.pos_hint = {'right_x': .5, 'bottom_y': .5}

        # Sample players
        player_names = ["Prof", "Django", "ZeltaVoid", "xXxSlayerxXx", "Init69", "Mao"]
        player_roles = ["Paladin", "Magus", "Druid", "Alchemist", "Summoner", "Fighter", "Elitist"]
        sample_portrait = ["src/images/portrait1.gif", "src/images/portrait2.gif", "src/images/portrait3.gif",
                           "src/images/portrait7.gif", "src/images/portrait4.gif", "src/images/portrait5.gif",
                           "src/images/portrait6.gif"]
        for i in range(0, player_amount):
            current_player = player_names.pop()
            current_role = player_roles.pop()
            current_image = sample_portrait.pop()
            self.player = Player(current_image, current_player, current_role, "0/1000", "0/100")
            self.add_widget(self.player)

'''
    This class defines a single 'other player' Rectangle, the ones you see to the right
    of the screen. Here you can change what should be displayed, such as the current:
                                            Player name, Player role, Player portrait
'''
class Player(GridLayout):
    def __init__(self, portrait, name, role, health, mana, **kwargs):
        super(Player, self).__init__(**kwargs)
        color = (random(), 1, 1, .3)
        with self.canvas:
            Color(*color, mode='hsv')  # Black with 50 Opacity (RBGA)
            self.rect = Rectangle(source='src/images/texture.jpg',
                                  pos=self.center,
                                  size=(self.width, self.height))
            print self.rect.size

        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

        self.name = Label(text=name)
        self.image = Image(source=portrait)
        self.role = Label(text=role)
        self.health = Label(text=health)
        self.mana = Label(text=mana)

        self.cols = 3

        self.role_box = BoxLayout(orientation="vertical")
        self.stats_box = BoxLayout(orientation="vertical")
        self.role_box.add_widget(self.name)
        self.role_box.add_widget(self.role)
        self.stats_box.add_widget(self.health)
        self.stats_box.add_widget(self.mana)

        self.add_widget(self.role_box)
        self.add_widget(self.stats_box)
        self.add_widget(self.image)

        print self.name

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            GamePlayerScreen.target_character_box.clear_widgets()
            target_character = Player(self.image.source, self.name.text, self.role.text, self.health.text, self.mana.text)
            GamePlayerScreen.target_character_box.add_widget(target_character)









