from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

class HomeScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        self.add_widget(Image(source='background.jpg', allow_stretch=True, keep_ratio=False))

        label = Label(text='I was built in python!', font_size='20sp', size_hint=(.25, .10), pos_hint={'center_x' : .5, 'center_y' : .70})
        self.add_widget(label)

        self.buttons = Buttons(size_hint=(.25, .15), pos_hint={'center_x' : .5, 'center_y' : .5})
        self.add_widget(self.buttons)

        self.quit_button = Button(text='Quit', size_hint=(.10, .05), pos_hint={'center_x' : .95, 'bottom_y' : .025})
        self.add_widget(self.quit_button)

class Buttons(BoxLayout):
    def __init__(self, **kwargs):
        super(Buttons, self).__init__(**kwargs)
        self.orientation ='vertical'
        self.spacing = 5

        join_button = Button(text='Join')
        self.add_widget(join_button)

        host_button = Button(text='Host')
        self.add_widget(host_button)

        character_button = Button(text='Characters')
        self.add_widget(character_button)
