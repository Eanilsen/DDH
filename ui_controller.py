from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.app import App

#need to add a fail-safe here to avoid adding multiple menus with
#the same name
Builder.load_file("homescreen.kv")
Builder.load_file("joinscreen.kv")

class HomeScreen(Screen):
    pass


class JoinScreen(Screen):
    pass

sm = ScreenManager(transition=NoTransition())
home = HomeScreen(name='home')
join = JoinScreen(name='join')
sm.add_widget(home)
sm.add_widget(join)

class MyApp(App):
    def build(self):
        return sm

if __name__=='__main__':
    MyApp().run()