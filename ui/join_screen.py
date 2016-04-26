from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen

#Sample screen to test switching between layouts

class JoinScreen(Screen):
    def __init__(self, **kwargs):
        super(JoinScreen, self).__init__(**kwargs)

        self.add_widget(Image(source='background.jpg', allow_stretch=True, keep_ratio=False))

        self.back_button = Button(text='back');

        self.add_widget(self.back_button)
