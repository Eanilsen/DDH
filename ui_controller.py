from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.app import App
from kivy.lang import Builder


Builder.load_file("homescreen.kv")
Builder.load_file("joinscreen.kv")

sm = ScreenManager(transition=NoTransition())
home = HomeScreen(name='home')
join = OtherScreen(name='join')
sm.add_widget(home)
sm.add_widget(join)

class MyApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    MyApp().run()