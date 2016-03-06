from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

#Note that the name of the .kv file MUST be same as the class we are running
class HomeScreen(App):
    def build(self):
        return FloatLayout()

if __name__=='__main__':
    HomeScreen().run()