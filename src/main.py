from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.app import App
from ui.home_screen import HomeScreen
from ui.join_screen import JoinScreen
from ui.character_screen import CharacterScreen

sm = ScreenManager(transition=NoTransition())

class Home(HomeScreen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        self.join_button.bind(on_release=switch_to_join)
        self.character_button.bind(on_release=switch_to_char)
        self.quit_button.bind(on_release=exit_application);

class Join(JoinScreen):
    def __init__(self, **kwargs):
        super(Join, self).__init__(**kwargs)
        self.back_button.bind(on_release=switch_to_home)

class Character(CharacterScreen):
    def __init__(self, **kwargs):
        super(Character, self).__init__(**kwargs)
        self.back_button.bind(on_release=switch_to_home)

def switch_to_join(*args):
    sm.current = 'join'

def switch_to_home(*args):
    sm.current = 'home'

def switch_to_char(*args):
    sm.current = 'char'

def exit_application(*args):
    #This wrapper is necessary because storing exit(0) in on_release will
    #exit the program immediatly after launch. Aslo, consider adding 
    #more sophisticated error handling.
    exit(0);

home = Home(name='home')
sm.add_widget(home)

join = Join(name='join')
sm.add_widget(join)

char = Character(name='char')
sm.add_widget(char)

class MyApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    MyApp().run()
