from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.app import App
from os import listdir
import sys

#add all the kv files in the current directory to the screenmanager
Builder.load_file("main.kv")
class HomeScreen(Screen):
    pass

class JoinScreen(Screen):
    pass
# Define functions in this class to call them with root.function() in HostScreen.kv
class HostScreen(Screen):
    def set_text(self, text):
        sm.get_screen("game").ids.server_name.text = text

class GameScreen(Screen):
    pass

class CharacterScreen(Screen):
    pass
  
sm = ScreenManager(transition=NoTransition())
home = HomeScreen()
join = JoinScreen()
<<<<<<< HEAD:ui/ui_controller.py
char = CharacterScreen()
sm.add_widget(home)
sm.add_widget(join)
sm.add_widget(char)
=======
host = HostScreen()
game = GameScreen()

sm.add_widget(home)
sm.add_widget(join)
sm.add_widget(host)
sm.add_widget(game)

def get_sm():
    return sm
>>>>>>> develop:src/main.py

class DDH(App):
    def build(self):
        return sm

<<<<<<< HEAD:ui/ui_controller.py
if __name__=='__main__':
    MyApp().run()
=======
if __name__ == '__main__':
    DDH().run()
>>>>>>> develop:src/main.py
