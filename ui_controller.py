from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.app import App
from home_screen import HomeScreen
from join_screen import JoinScreen

sm = ScreenManager(transition=NoTransition())

class Home(HomeScreen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        self.join_button.bind(on_release=switch_to_join)

class Join(JoinScreen):
    def __init__(self, **kwargs):
        super(Join, self).__init__(**kwargs)
        self.back_button.bind(on_release=switch_to_home)


def switch_to_join(*args):
    sm.current = 'join'

def switch_to_home(*args):
    sm.current = 'home'


home = Home(name='home')
sm.add_widget(home)

join = Join(name='join')
sm.add_widget(join)

class MyApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    MyApp().run()
