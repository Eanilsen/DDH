from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.app import App
from os import listdir
import sys

#add all the kv files in the current directory to the screenmanager
for f in listdir("."):
    if f.lower().endswith(".kv"):
        Builder.load_file(f)

class HomeScreen(Screen):
    pass

class JoinScreen(Screen):
    pass


# Define functions in this class to call them with root.function() in HostScreen.kv
class HostScreen(Screen):
    def printSomething(self):
        print "Something - Simen F. 2016"
    def printTextToConsole(self, text):
        print text

class GameScreen(Screen):
    pass


sm = ScreenManager(transition=NoTransition())
home = HomeScreen()
join = JoinScreen()
host = HostScreen()
game = GameScreen()

sm.add_widget(home)
sm.add_widget(join)
sm.add_widget(host)
sm.add_widget(game)

class MyApp(App):
    def build(self):
        return sm



if __name__ == '__main__':
    MyApp().run()