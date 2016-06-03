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

class WeaponTab(TabbedPanelHeader):
    
    all_weapons = [
        'Axe',
        'Brass Knife',
        'Bayonet',
        'Club',
        'Crossbow',
        'Cutlass',
        'Dart',
        'Flail',
        'Gladius',
        'Greatsword',
        'Handaxe',
        'Kama',
        'Knife',
        'Lance',
        'Longbow',
        'Pickaxe',
        'Scythe',
        'Spear',
        'Shortsword',
        'Warhammer'
        ]
    weapon_list = []
    weapon_overview = BoxLayout(orientation='vertical')
    weapon_box = BoxLayout(
            orientation='vertical',
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=5)
    weapons_owned = []
    
    def __init__(self, **kwargs):
        global popup
        super(WeaponTab, self).__init__(**kwargs)
        
        add_weapon_button = Button(
            text='Add Weapon',
            size_hint=(.2, .05),
            pos_hint={'center_x': .5, 'center_y': .1})
        print popup
        popup = self.create_popup()
        add_weapon_button.bind(on_press=popup.open)
        
        content = FloatLayout()
        content.add_widget(self.weapon_box)
        content.add_widget(add_weapon_button)
        
        self.content=content
        self.text = 'Weapon'
        
    def create_popup(self):
        content = BoxLayout(orientation='vertical', spacing=10)
        select_button = Button(
            size_hint=(.5, .2),
            text='Select',
            pos_hint={'center_x': .5, 'center_y': .2});
            
        content.add_widget(self.weapon_overview)
        
        popup = Popup(
            title='Select a weapon',
            content=content,
            size_hint=(.8, .8))
        for weapon in self.all_weapons:
            label = WeaponLabel(text=weapon)
            self.weapon_overview.add_widget(label)
            self.weapon_list.append(label)
        return popup
        
class WeaponLabel(Label):
    def __init__(self, **kwargs):
        super(WeaponLabel, self).__init__(**kwargs)
        self.highlighted = False
        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.clear_highlights(self)
            if touch.is_double_tap:
                if 2 < len(WeaponTab.weapons_owned):
                    self.display_too_many_weapons()
                    popup.dismiss()
                    return
                else:
                    weapon = BoxLayout(
                        orientation='horizontal')
                    weapon_label = Label(text=self.text)
                    weapon_dmg = TextInput(
                        multiline=False,
                        hint_text='dmg',
                        size_hint=(.8, .5),
                        pos_hint={'center_x': .5, 'center_y': .6})
                    weapon_crit = TextInput(
                        multiline=False,
                        hint_text='crit',
                        size_hint=(.8, .5),
                        pos_hint={'center_x': .5, 'center_y': .6})
                    weapon_range = TextInput(
                        multiline=False,
                        hint_text='range',
                        size_hint=(.8, .5),
                        pos_hint={'center_x': .5, 'center_y': .6})
                    weapon_type = TextInput(
                        multiline=False,
                        hint_text='type',
                        size_hint=(.8, .5),
                        pos_hint={'center_x': .5, 'center_y': .6})
                    weapon.add_widget(weapon_label)
                    weapon.add_widget(weapon_dmg)
                    weapon.add_widget(weapon_crit)
                    weapon.add_widget(weapon_range)
                    weapon.add_widget(weapon_type)
                    WeaponTab.weapon_box.add_widget(weapon)
                    WeaponTab.weapons_owned.append(self)
                    popup.dismiss()
            else:
                with self.canvas:
                    
                    Color(255, 255, 250, .3)
                    self.rectangle = Rectangle(pos=(self.x, self.y),
                        size=(self.width, self.height))
                    self.highlighted  = True
    
    def display_too_many_weapons(self):
        layout = FloatLayout()
        popup = Popup(
            content=layout,
            size_hint=(.5, .5),
            title='Cannot add Weapon')
        label = Label(
            text="You have cannot own more weapons",
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
        for s in WeaponTab.weapon_list:
            if s.highlighted and s != self:
                s.canvas.remove(s.rectangle)
                s.highlighted = False
        
