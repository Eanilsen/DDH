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

class SkillsTab(TabbedPanelHeader):
    
    all_skills = [
        'Acrobatics',
        'Appraise',
        'Bluff',
        'Climb',
        'Craft',
        'Diplomacy',
        'Disable Device',
        'Disguise',
        'Escape Artist',
        'Fly',
        'Handle Animal',
        'Heal',
        'Intimidate',
        'Knowledge',
        'Linguistics',
        'Perception',
        'Perform',
        'Profession',
        'Ride',
        'Sense Motive',
        'Sleight of Hand',
        'Spellcraft',
        'Stealth',
        'Survival',
        'Swim',
        'Use Magic Device'
        ]
    skills_list = []
    skills_overview = BoxLayout(orientation='vertical')
    skills_box = BoxLayout(
            orientation='vertical',
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=5)
    
    def __init__(self, **kwargs):
        global popup
        super(SkillsTab, self).__init__(**kwargs)
        
        add_skill_button = Button(
            text='Add Skill',
            size_hint=(.2, .05),
            pos_hint={'center_x': .5, 'center_y': .1})
        print popup
        popup = self.create_popup()
        add_skill_button.bind(on_press=popup.open)
        
        content = FloatLayout()
        content.add_widget(self.skills_box)
        content.add_widget(add_skill_button)
        
        self.content=content
        self.text = 'Skills'
        
    def create_popup(self):
        content = BoxLayout(orientation='vertical', spacing=10)
        select_button = Button(
            size_hint=(.5, .2),
            text='Select',
            pos_hint={'center_x': .5, 'center_y': .2});
            
        content.add_widget(self.skills_overview)
        
        popup = Popup(
            title='Select a skill',
            content=content,
            size_hint=(.8, .8))
        for skill in self.all_skills:
            label = SkillLabel(text=skill)
            self.skills_overview.add_widget(label)
            self.skills_list.append(label)
        return popup
        
class SkillLabel(Label):
    def __init__(self, **kwargs):
        super(SkillLabel, self).__init__(**kwargs)
        self.highlighted = False
        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.clear_highlights(self)
            if touch.is_double_tap:
                new_skill = BoxLayout(orientation='horizontal')
                new_skill_label = Label(text=self.text)
                new_skill_text_input = TextInput(
                    multiline=False, text_hint='Notes')
                new_skill.add_widget(new_skill_label)
                new_skill.add_widget(new_skill_text_input)
                SkillsTab.skills_box.add_widget(new_skill)
                popup.dismiss()
            else:
                with self.canvas:
                    
                    Color(255, 255, 250, .3)
                    self.rectangle = Rectangle(pos=(self.x, self.y),
                        size=(self.width, self.height))
                    self.highlighted  = True
                
    def clear_highlights(self, *args):
        for s in SkillsTab.skills_list:
            if s.highlighted and s != self:
                s.canvas.remove(s.rectangle)
                s.highlighted = False
        
