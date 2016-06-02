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
from kivy.uix.dropdown import DropDown  # Used for dropdown
from random import random, shuffle

class GamePlayerScreen(Screen):
    def __init__(self, **kwargs):
        super(GamePlayerScreen, self).__init__(**kwargs)
        self.background = Image(source='images/background.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)
        # Create an outer layout for structure
        self.outer_layout = BoxLayout(orientation='vertical')
        # Create a bottom container, as opposite to the CharacterInformation() at the top
        self.bottom_container = BoxLayout(orientation='horizontal',
                                          spacing=50)  # Spacing between tabbed_panel and all_players
        self.add_widget(self.outer_layout)
        # Add the tabbed container to the bottom layout
        self.bottom_container.add_widget(TabbedActivityContainer())
        # Add the player panel to the bottom layout
        self.bottom_container.add_widget(PlayersPanel(6))
        # This is the top container which holds character_information as opposite to the bottom container
        self.outer_layout.add_widget(CharacterInformation("images/portrait1.gif",
                                                          "Character Name",
                                                          "1337/2000",
                                                          "105/200"))
        # modular_panel holds the tabbed_panel and all_players containers
        self.outer_layout.add_widget(self.bottom_container)

class CharacterInformation(BoxLayout):
    def __init__(self, portrait, player_name, player_health, player_mana, **kwargs):
        super(CharacterInformation, self).__init__(**kwargs)

        self.orientation = 'horizontal'
        self.size_hint = (1, .12)
        self.character = Image(source=portrait)
        self.player_name = Label(text=player_name)
        self.player_health = Label(text=player_health)
        self.player_mana = Label(text=player_mana)
        text_box = BoxLayout(orientation='vertical')
        text_box.add_widget(self.player_name)
        text_box.add_widget(self.player_health)
        text_box.add_widget(self.player_mana)

        self.add_widget(self.character)
        self.add_widget(text_box)

'''
    This is the tabbed container. Most of the information from Character Sheets
    are displayed in the different tabs. You can choose what you want to view at any time.
    for documentation: https://kivy.org/docs/api-kivy.uix.tabbedpanel.html
'''
class TabbedActivityContainer(TabbedPanel):
    def __init__(self, **kwargs):
        super(TabbedActivityContainer, self).__init__(**kwargs)

        self.tab_pos = 'top_left'
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
        sample_portrait = ["images/portrait1.gif", "images/portrait2.gif", "images/portrait3.gif", "images/portrait7.gif",
                           "images/portrait4.gif", "images/portrait5.gif", "images/portrait6.gif"]
        for i in range(0, player_amount):
            current_player = player_names.pop()
            current_role = player_roles.pop()
            current_image = sample_portrait.pop()
            self.player = Player(current_image, current_player, current_role)
            self.add_widget(self.player)

'''
    This class defines a single 'other player' Rectangle, the ones you see to the right
    of the screen. Here you can change what should be displayed, such as the current:
                                            Player name, Player role, Player portrait
'''
class Player(GridLayout):
    def __init__(self, image, name, role, **kwargs):
        super(Player, self).__init__(**kwargs)
        color = (random(), 1, 1, .5)
        with self.canvas:
            Color(*color, mode='hsv')  # Black with 50 Opacity (RBGA)
            self.rect = Rectangle(source='images/texture.jpg',
                                  pos=self.center,
                                  size=(self.width, self.height))
            print self.rect.size

        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

        self.name = Label(text=name)
        self.image = Image(source=image)
        self.role = Label(text=role)
        self.cols = 3

        self.add_widget(self.name)
        self.add_widget(self.role)
        self.add_widget(self.image)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
