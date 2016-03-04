from kivy.app import App
from home_screen import HomeScreen

#Put calls to initalize backend here, if needed

class Launcher(App):
    def build(self):
        return HomeScreen()

if __name__ == '__main__':
    Launcher().run()