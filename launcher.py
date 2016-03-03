from kivy.app import App
import home_screen

#Put calls to initalize backend here, if needed

class Launcher(App):
    def build(self):
        return home_screen.get_home_screen()

if __name__ == '__main__':
    Launcher().run()