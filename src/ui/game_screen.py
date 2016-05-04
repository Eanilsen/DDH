from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.graphics import *

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.background = Image(source='images/background.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)
        with self.canvas:
            Color(0, 0, 0, .5)  # Black with 50 Opacity (RBGA)
            Rectangle(pos=self.pos, size=self.size)

        self.outer_layout = BoxLayout(orientation='vertical')
        self.player_info_box = BoxLayout(orientation='horizontal', spacing=30, size_hint=(1, None), height=80)
        with self.canvas:
            Color(1, 1, 1, .5)
            Rectangle(self.pos, self.size)
        self.image = Image(size_hint=None, None), size=80, 80, source=images/char.jpg



"""
<GameScreen>
    name: "game"

    BoxLayout:
        id: outer_layout
        orientation: 'vertical'

        BoxLayout:
            id: player_info
            orientation: 'horizontal'
            spacing: 30
            size_hint: 1, None
            height: 80
            canvas:
                Color:
                    rgba: 1, 1, 1, .5
                Rectangle:
                    pos: self.pos
                    size: self.size
            Image:
                size_hint: None, None
                size: 80, 80
                source: 'images/char.jpg'
            Label:
                text: 'Character Name'

        BoxLayout:
            id: modular_panel
            orientation: 'horizontal'
            # https://kivy.org/docs/api-kivy.uix.tabbedpanel.html
            TabbedPanel:
                tab_pos: 'top_left'
                do_default_tab: False

                TabbedPanelItem:
                    text: 'Magic'
                    Label:
                        text: 'Add for example magic information here.'

                TabbedPanelItem:
                    text: 'Useful Info'
                    Label:

                    BoxLayout:
                        orientation: 'vertical'
                        Button:
                            size_hint: (.4, .3)
                            text: 'pls'
                        Button:
                            size_hint: (.4, .2)
                            text: 'add functions to me!'

                TabbedPanelItem:
                    text: 'Character Traits'
                    Label:
                        text: 'Add for example character stats here.'

            RelativeLayout:
                Label:
                    id: server_name
                    background: 'white'
                    text: 'Add health information here?'


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
