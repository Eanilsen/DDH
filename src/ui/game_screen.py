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

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.background = Image(source='images/background.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)
        with self.canvas:
            Color(0, 0, 0, .5)  # Black with 50 Opacity (RBGA)
            Rectangle(pos=self.pos, size=self.size)

        # Create character portrait, player name and the player_layout and add them together
        self.character = Image(size_hint=(None, None), size=(80, 80), source="images/char.jpg")
        self.player_name = Label(text='Character Name')
        self.player_info_box = BoxLayout(orientation='horizontal', spacing=30, size_hint=(1, None), height=80)
        with self.canvas:
            Color(1, 1, 1, .5) #TODO Make the canvas display in the upper left corner, not in the bottom!
            Rectangle(pos=self.pos, size=self.size)
        self.player_info_box.add_widget(self.player_name)
        self.player_info_box.add_widget(self.character)

        # Create 3 tabs and add them to a TabbedPanel, then add it to a modular_panel
        self.tab1 = TabbedPanelItem(text='Magic')
        self.tab1.add_widget(Label(text='Add magic information here'))

        self.tab2 = TabbedPanelItem(text='Useful Info')
        self.tab2.add_widget(Label(text='Add some useful information to display in tab 2'))

        self.tab3 = TabbedPanelItem(text='Character Traits')
        self.tab3.add_widget(Label(text='Add traits here'))

        self.tabbed_panel = TabbedPanel(tab_pos='top_left', do_default_tab=False)
        self.tabbed_panel.add_widget(self.tab1)
        self.tabbed_panel.add_widget(self.tab2)
        self.tabbed_panel.add_widget(self.tab3)

        # Create information about other players
        self.player1 = Player("images/char.jpg", "Player 1")
        self.player2 = Button(text='Player 2', size_hint=(.6, .1))
        self.player3 = Button(text='Player 3', size_hint=(.6, .1))
        self.player4 = Button(text='Player 4', size_hint=(.6, .1))
        self.all_players = BoxLayout(orientation='vertical', spacing=1)
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

class Player(object):
    def __init__(self, image, name, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.image = Image(source=image)
        self.name = Label(text=name)

        grid = GridLayout(cols=2,
                          row_force_default=True,
                          row_default_height=40,
                          row_default_width=120)
        grid.add_widget(self.image)
        grid.add_widget(self.name)









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