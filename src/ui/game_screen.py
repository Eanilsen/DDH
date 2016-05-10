from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.graphics import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.background = Image(source='images/background.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)

        # Create character portrait, player name and the player_layout and add them together
        self.character = Image(source="images/char.jpg",
                               size_hint=(1, 1),
                               pos_hint={'left_x': .1, 'center_y': .4})
        self.player_name = Label(text='Character Name')
        self.player_info_box = BoxLayout(orientation='horizontal',
                                         spacing=20,
                                         size_hint=(1, None),
                                         height=120)

        self.player_info_box.add_widget(self.character)
        self.player_info_box.add_widget(self.player_name)

        # Create 3 tabs and add them to a TabbedPanel, then add it to a modular_panel
        self.tab1 = TabbedPanelItem(text='Magic')
        self.tab1.add_widget(Label(text='Add magic information here'))

        self.tab2 = TabbedPanelItem(text='Useful Info')
        self.tab2.add_widget(Label(text='Add some useful information to display in tab 2'))

        self.tab3 = TabbedPanelItem(text='Character Traits')
        self.tab3.add_widget(Label(text='Add traits here'))

        self.tabbed_panel = TabbedPanel(tab_pos='top_left',
                                        do_default_tab=False)
        self.tabbed_panel.add_widget(self.tab1)
        self.tabbed_panel.add_widget(self.tab2)
        self.tabbed_panel.add_widget(self.tab3)

        # Create information about other players
        self.player1 = Player("images/char.jpg", "Player 1", "Paladin")
        self.player2 = Player("images/char.jpg", "Player 2", "Magus")
        self.player3 = Player("images/char.jpg", "Player 3", "Archer")
        self.player4 = Player("images/char.jpg", "Player 4", "Alchemist")
        self.all_players = BoxLayout(orientation='vertical',
                                     spacing=10,
                                     size_hint=(.2, .2),
                                     pos_hint={'right_x': .5, 'center_y': .8})
        self.all_players.add_widget(self.player1)
        self.all_players.add_widget(self.player2)
        self.all_players.add_widget(self.player3)
        self.all_players.add_widget(self.player4)

        self.modular_panel = BoxLayout(orientation='horizontal')
        self.modular_panel.add_widget(self.tabbed_panel)
        self.modular_panel.add_widget(self.all_players)

        # Create the outer_layout and add layouts to it
        self.outer_layout = BoxLayout(orientation='vertical')
        self.add_widget(self.outer_layout)
        self.outer_layout.add_widget(self.player_info_box)

        self.outer_layout.add_widget(self.modular_panel)

class Player(GridLayout):
    def __init__(self, image, name, role, **kwargs):
        super(Player, self).__init__(**kwargs)
        self.name = Label(text=name)
        self.image = Image(source=image)
        self.role = Label(text=role)

        self.cols = 3
        self.row_force_default = True
        self.row_default_height = 40
        self.row_default_width = 60

        self.add_widget(self.image)
        self.add_widget(self.name)
        self.add_widget(self.role)

        with self.canvas:
            Color(0, 0, 0, .5)  # Black with 50 Opacity (RBGA)
            self.rect = Rectangle(pos=self.center,
                                  size=(self.width / 1, self.height / 1))

        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size








""" This is how the old .kv made the buttons drag able:

            BoxLayout: # Current Players
                orientation: 'vertical'
                id: 'players'
                spacing: 1
                Scatter:
                    do_scale: False
                    do_rotation: False

                Button:
                    text: 'Player 1'
                Button:
                    text: 'Player 2'
                Button:
                    text: 'Player 3'

                # Define the root widget
                DragLabel:
                    text: 'Drag me'
                Button:
                    text: 'Player 4'
                    on_touch_down: print('Right: {}'.format(args[1].pos))
                DragLabel:
                    text: "Don't push me"
                    drag_rect_y: modular_panel.height
                    drag_rect_x: modular_panel.width

# For changing visuals of the tabs bar
<TabbedPanelStrip>:
    canvas:
        Color:
            rgba: (0, 1, 0, 1) # green
        Rectangle:
            size: self.size
            pos: self.pos

<DragLabel>:
    # Define the properties for the DragLabel
    drag_rectangle: self.x, self.y, self.width, self.height
    drag_timeout: 10000000
    drag_distance: 0 # Before widget starts being dragged
"""