from nose.tools import *
from kivy.uix.screenmanager import Screen, ScreenManager
from ui.home_screen import HomeScreen
from ui.join_screen import JoinScreen

def test_homescreen():
    hs = HomeScreen()
    isinstance(hs, Screen)
    assert_equal(hs.label.text, 'Welcome to DDH')
    assert_equal(hs.join_button.text, 'Join')
    assert_equal(hs.host_button.text, 'Host')
    assert_equal(hs.character_button.text, 'Characters')
    assert_equal(hs.quit_button.text, 'Quit')
    assert_equal(hs.buttons.orientation, 'vertical')
    assert_equal(hs.buttons.spacing, 5)
    assert_equal(hs.background.source, 'images/background.jpg')

def test_joinscreen():
    js = JoinScreen()
    isinstance(js, Screen)
    assert_equal(js.background.source, 'images/background.jpg')
    #no need to test joinscreen further, is only a placeholder

def test_main():
    import main
    sm = main.sm
    isinstance(sm, ScreenManager)

    home = main.home
    isinstance(home, HomeScreen)
    assert_equal(home.name, 'home')

    join = main.join
    isinstance(join, JoinScreen)
    assert_equal(join.name, 'join')
