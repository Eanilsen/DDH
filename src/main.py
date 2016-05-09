from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.app import App
from ui.home_screen import HomeScreen
from ui.join_screen import JoinScreen
from ui.host_screen import HostScreen
from ui.game_screen import GameScreen

sm = ScreenManager(transition=NoTransition())

class Home(HomeScreen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        self.join_button.bind(on_release=switch_to_join)
        self.host_button.bind(on_release=switch_to_host_screen)
        self.quit_button.bind(on_release=exit_application)

class Join(JoinScreen):
    def __init__(self, **kwargs):
        super(Join, self).__init__(**kwargs)
        self.back_button.bind(on_release=switch_to_home)

class Host(HostScreen):
    def __init__(self, **kwargs):
        super(Host, self).__init__(**kwargs)
        self.back_button.bind(on_release=switch_to_home)
        self.host_game_button.bind(on_release=switch_to_game_screen)

class Game(GameScreen):
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)

def switch_to_join(*args):
    sm.current = 'join'

def switch_to_home(*args):
    sm.current = 'home'

def switch_to_host_screen(*args):
    sm.current = 'host'

def switch_to_game_screen(*args):
    sm.current ='game'

def exit_application(*args):
    """This wrapper is necessary because storing exit(0) in on_release will
        exit the program immediatly after launch. Aslo, consider adding
        more sophisticated error handling."""
    exit(0)

home = Home(name='home')
sm.add_widget(home)

join = Join(name='join')
sm.add_widget(join)

host = Host(name='host')
sm.add_widget(host)

game = Game(name='game')
sm.add_widget(game)

class MyApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    MyApp().run()
