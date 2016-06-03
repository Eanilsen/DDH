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
from src.util import filehandler
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
            source="src/images/background.jpg",
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
            font_name='src/fonts/Enchanted_Land.otf',
            font_size=24,
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

        save_button = Button(
            font_name='src/fonts/Enchanted_Land.otf',
            font_size=24,
            text='Save')
        save_button.bind(on_release=self.save_sheet)
        buttons.add_widget(save_button)

        new_button = Button(
            font_name='src/fonts/Enchanted_Land.otf',
            font_size=24,
            text='New')
        buttons.add_widget(new_button)

        file_handler = filehandler.FileHandler()
        load_button = Button(
            font_name='src/fonts/Enchanted_Land.otf',
            font_size=24,
            text='Load')
        load_button.bind(on_release=file_handler.show_load_popup)
        buttons.add_widget(load_button)

        return buttons

    def create_sheet(self):
        character_sheet = TabbedPanel(
            tab_pos='top_mid',
            size_hint=(.85,.85),
            pos_hint={'center_x': .5, 'center_y': .5},
            do_default_tab=False)
        general_tab = GeneralTab(
            font_name='src/fonts/Enchanted_Land.otf',
            font_size=24)

        self.panes.append(general_tab)

        attributes_tab = AttributesTab(
            font_name='src/fonts/Enchanted_Land.otf',
            font_size=24)
        self.panes.append(attributes_tab)

        skills_tab = SkillsTab(
            font_name='src/fonts/Enchanted_Land.otf',
            font_size=24)
        self.panes.append(skills_tab)

        weapon_tab = WeaponTab(
            font_name='src/fonts/Enchanted_Land.otf',
            font_size=24)
        self.panes.append(weapon_tab)

        armor_tab = ArmorTab(
            font_name='src/fonts/Enchanted_Land.otf',
            font_size=24)
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
        spells = TabbedPanelHeader(
            font_name='src/fonts/Enchanted_Land.otf',
            font_size=24,
            text='Spells')
        return spells

    def general_make_serializable(self):
        general_dict = {}
        general_dict['name'] = self.panes[0].name_input.text
        general_dict['alignment'] = self.panes[0].alignment_input.text
        general_dict['class'] = self.panes[0].class_input.text
        general_dict['level'] = self.panes[0].level_input.text
        general_dict['gender'] = self.panes[0].gender_input.text
        general_dict['race'] = self.panes[0].race_input.text
        general_dict['age'] = self.panes[0].age_input.text
        general_dict['height'] = self.panes[0].height_input.text
        general_dict['weight'] = self.panes[0].weight_input.text
        general_dict['size'] = self.panes[0].size_input.text
        return general_dict

    def save_sheet(self, *args):
        file_handler = filehandler.FileHandler()
        save_dict = self.general_make_serializable()
        file_handler.show_save_popup(save_dict)

