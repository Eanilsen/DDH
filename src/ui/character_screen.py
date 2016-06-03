from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from util import filehandler
from skills_tab import SkillsTab
from general_tab import GeneralTab
from attributes_tab import AttributesTab
from weapon_tab import WeaponTab
from armor_tab import ArmorTab

class CharacterScreen(Screen):
    def __init__(self, **kwargs):
        super(CharacterScreen, self).__init__(**kwargs)
        self.add_widget(Image(
            #change to src
            source="images/background.jpg",
            allow_stretch=True,
            keep_ratio=False))

        self.layout = FloatLayout()
        self.add_widget(self.layout)

        self.panes = []

        sheet = self.create_sheet()
        self.layout.add_widget(sheet)

        buttons = self.create_buttons()
        self.add_widget(buttons)

        self.back_button = Button(
            text='Back',
            size_hint=(.10, .05),
            pos_hint={'center_x' : .95, 'bottom_y' : .025})

        self.add_widget(self.back_button)

    def create_buttons(self):
        buttons = BoxLayout(
            orientation='horizontal',
            size_hint=(.5, .05),
            pos_hint={'center_x': .325, 'center_y': .1},
            spacing=15)

        save_button = Button(text='Save')
        buttons.add_widget(save_button)

        new_button = Button(text='New')
        buttons.add_widget(new_button)

        load_button = Button(text='Load')
        buttons.add_widget(load_button)

        return buttons

    def create_sheet(self):
        character_sheet = TabbedPanel(
            tab_pos='top_mid',
            size_hint=(.85,.85),
            pos_hint={'center_x': .5, 'center_y': .5},
            do_default_tab=False)
        general_tab = GeneralTab()
        self.panes.append(general_tab)

        attributes_tab = AttributesTab()
        self.panes.append(attributes_tab)

        skills_tab = SkillsTab()
        self.panes.append(skills_tab)

        weapon_tab = WeaponTab()
        self.panes.append(weapon_tab)
        
        armor_tab = ArmorTab()
        self.panes.append(armor_tab)

        spells_tab = self.create_spells()
        self.panes.append(spells_tab)

        character_sheet.add_widget(general_tab)
        character_sheet.add_widget(attributes_tab)
        #NOTE ADD FEATS TO SKILLS
        character_sheet.add_widget(skills_tab)
        character_sheet.add_widget(weapon_tab)
        character_sheet.add_widget(armor_tab)
        character_sheet.add_widget(spells_tab)

        return character_sheet
    
    def create_spells(self):
        spells = TabbedPanelHeader(text='Spells')
        return spells


