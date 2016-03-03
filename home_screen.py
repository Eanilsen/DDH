from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class HomeScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        label = Label(text='Welcome to DDH!', size_hint=(.25, .10), pos_hint={'center_x' : .5, 'center_y' : .70})
        self.add_widget(label)

        self.join_button = Buttons(size_hint=(.25, .10), pos_hint={'center_x' : .5, 'center_y' : .5})
        self.add_widget(self.join_button)

        quit_button = Button(text='Quit', size_hint=(.10, .05), pos_hint={'center_x' : .95, 'bottom_y' : .025})
        self.add_widget(quit_button)

class Buttons(BoxLayout):
    def __init__(self, **kwargs):
        super(Buttons, self).__init__(**kwargs)
        self.orientation ='vertical'
        join_button = Button(text='join')
        self.add_widget(join_button)
        host_button = Button(text='host')
        self.add_widget(host_button)

def get_home_screen():
    return HomeScreen()
