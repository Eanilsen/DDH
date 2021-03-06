from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.app import App
from src.ui.home_screen import HomeScreen
from src.ui.join_screen import JoinScreen
from src.ui.host_screen import HostScreen
from src.ui.game_player_screen import GamePlayerScreen
from src.ui.game_master_screen import GameMasterScreen
from src.ui.character_screen import CharacterScreen

sm = ScreenManager(transition=NoTransition())

class Home(HomeScreen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        self.join_button.bind(on_release=switch_to_join)
        self.host_button.bind(on_release=switch_to_host_screen)
        self.quit_button.bind(on_release=exit_application)
        self.character_button.bind(on_release=switch_to_character_screen)

class Join(JoinScreen):
    def __init__(self, **kwargs):
        super(Join, self).__init__(**kwargs)
        self.back_button.bind(on_release=switch_to_home)
        self.join_button.bind(on_release=switch_to_game_player_screen)

class Host(HostScreen):
    def __init__(self, **kwargs):
        super(Host, self).__init__(**kwargs)
        self.back_button.bind(on_release=switch_to_home)
        self.start_game_button.bind(on_release=switch_to_game_master_screen)

class GamePlayer(GamePlayerScreen):
    def __init__(self, **kwargs):
        super(GamePlayer, self).__init__(**kwargs)

class GameMaster(GameMasterScreen):
    def __init__(self, **kwargs):
        super(GameMaster, self).__init__(**kwargs)
        self.back_button.bind(on_release=switch_to_home)
        print self.back_button.text

    def test(self):
        print "test"

class Character(CharacterScreen):
    def __init__(self, **kwargs):
        super(Character, self).__init__(**kwargs)
        self.back_button.bind(on_release=switch_to_home)

class Players(object):
    pass

def switch_to_join(*args):
    sm.current = 'join'

def switch_to_home(*args):
    sm.current = 'home'

def switch_to_host_screen(*args):
    sm.current = 'host'

def switch_to_game_player_screen(*args):
    sm.current = 'game_player'

def switch_to_game_master_screen(*args):
    sm.current = 'game_master'

def switch_to_character_screen(*args):
    sm.current = 'character'

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

game_player = GamePlayerScreen(name='game_player')
sm.add_widget(game_player)

game_master = GameMasterScreen(name='game_master')
sm.add_widget(game_master)

character = Character(name='character')
sm.add_widget(character)

class MyApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    MyApp().run()
