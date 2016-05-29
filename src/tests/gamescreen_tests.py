from nose.tools import *
from kivy.uix.screenmanager import Screen, ScreenManager
from ui.game_screen import GameScreen, MagicTab

def test_game_screen():

    gs = GameScreen()
    mt = MagicTab()
    isinstance(gs, Screen)

    assert_equals(gs.outer_layout.orientation, 'vertical')
    # assert_equals(len(mt.spells), 8)
    # assert_equals(mt.spells[2], "Healing Rain")
