from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.graphics import Rectangle, Color

popup = None

class ArmorTab(TabbedPanelHeader):

    all_armors = [
        'Armorered Kilt',
        'Armored Coat',
        'Banded Mail',
        'Breastplate',
        'Buckler',
        'Chainmail',
        'Field Plate',
        'Heavy Wooden Sheild',
        'Hide Shirt',
        'Leaf Armor',
        'Light Steel Sheild',
        'Quilted  Armor',
        'Rosewood armor',
        'Scale mail',
        'Steel Shield',
        'Stoneplate',
        'Towershield',
        'Wooden Shield'
        ]
    armor_list = []
    armor_overview = BoxLayout(orientation='vertical')
    armor_box = BoxLayout(
            orientation='vertical',
            size_hint=(.8, .5),
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=5)
    armor_owned = []

    def __init__(self, **kwargs):
        global popup
        super(ArmorTab, self).__init__(**kwargs)

        add_armor_button = Button(
            text='Add Armor',
            size_hint=(.2, .05),
            pos_hint={'center_x': .5, 'center_y': .1})
        print popup
        popup = self.create_popup()
        add_armor_button.bind(on_press=popup.open)

        content = FloatLayout()
        content.add_widget(self.armor_box)
        content.add_widget(add_armor_button)

        self.content=content
        self.text = 'Armor'

    def create_popup(self):
        content = BoxLayout(orientation='vertical', spacing=10)
        select_button = Button(
            size_hint=(.5, .2),
            text='Select',
            pos_hint={'center_x': .5, 'center_y': .2});

        content.add_widget(self.armor_overview)

        popup = Popup(
            content=content,
            size_hint=(.8, .8))
        for armor in self.all_armors:
            label = ArmorLabel(text=armor)
            self.armor_overview.add_widget(label)
            self.armor_list.append(label)
        return popup

class ArmorLabel(Label):
    def __init__(self, **kwargs):
        super(ArmorLabel, self).__init__(**kwargs)
        self.highlighted = False

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.clear_highlights(self)
            if touch.is_double_tap:
                if 2 < len(ArmorTab.armor_owned):
                    self.display_too_much_armor()
                    popup.dismiss()
                    return
                else:
                    armor = BoxLayout(
                        orientation='horizontal')
                    armor_label = Label(text=self.text)
                    armor_bonus = TextInput(
                        multiline=False,
                        hint_text='bonus',
                        size_hint=(.8, .5),
                        pos_hint={'center_x': .5, 'center_y': .6})
                    armor_dex_bonus = TextInput(
                        multiline=False,
                        hint_text='dex bonus',
                        size_hint=(.8, .5),
                        pos_hint={'center_x': .5, 'center_y': .6})
                    armor_check_penalty = TextInput(
                        multiline=False,
                        hint_text='check penalty',
                        size_hint=(.8, .5),
                        pos_hint={'center_x': .5, 'center_y': .6})
                    armor_spell_failure = TextInput(
                        multiline=False,
                        hint_text='spell failure',
                        size_hint=(.8, .5),
                        pos_hint={'center_x': .5, 'center_y': .6})
                    armor_speed_30ft = TextInput(
                        multiline=False,
                        hint_text='speeed 30ft',
                        size_hint=(.8, .5),
                        pos_hint={'center_x': .5, 'center_y': .6})
                    armor_speed_20ft = TextInput(
                        multiline=False,
                        hint_text='speed 20ft',
                        size_hint=(.8, .5),
                        pos_hint={'center_x': .5, 'center_y': .6})

                    armor.add_widget(armor_label)
                    armor.add_widget(armor_bonus)
                    armor.add_widget(armor_dex_bonus)
                    armor.add_widget(armor_check_penalty)
                    armor.add_widget(armor_spell_failure)
                    armor.add_widget(armor_speed_30ft)
                    armor.add_widget(armor_speed_20ft)
                    ArmorTab.armor_box.add_widget(armor)
                    ArmorTab.armor_owned.append(self)
                    popup.dismiss()
            else:
                with self.canvas:

                    Color(255, 255, 250, .3)
                    self.rectangle = Rectangle(pos=(self.x, self.y),
                        size=(self.width, self.height))
                    self.highlighted  = True

    def display_too_much_armor(self):
        layout = FloatLayout()
        popup = Popup(
            content=layout,
            size_hint=(.5, .5),
            title='Cannot add Armor')
        label = Label(
            text="You have cannot have more armor",
            pos_hint={'center_x': .5, 'center_y': .8})
        button = Button(
            text='Close',
            size_hint=(.5, .2),
            pos_hint={'center_x': .5, 'center_y': .4})
        button.bind(on_press=popup.dismiss)
        layout.add_widget(label)
        layout.add_widget(button)
        popup.open()

    def clear_highlights(self, *args):
        for s in ArmorTab.armor_list:
            if s.highlighted and s != self:
                s.canvas.remove(s.rectangle)
                s.highlighted = False
