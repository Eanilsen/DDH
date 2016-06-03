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

class GeneralTab(TabbedPanelHeader):
    def __init__(self, **kwargs):
        super(GeneralTab, self).__init__(**kwargs)
        name_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        name_label = Label(
            text='Name',
            halign='right',
            valign='middle',
            text_size=self.size)
        self.name_input = TextInput(multiline=False)
        name_box.add_widget(name_label)
        name_box.add_widget(self.name_input)

        alignment_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        alignment_label = Label(
            text='Alignment',
            halign='right',
            valign='middle',
            text_size=self.size)
        self.alignment_input = TextInput(multiline=False)
        alignment_box.add_widget(alignment_label)
        alignment_box.add_widget(self.alignment_input)

        class_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        class_label = Label(
            text='Class',
            halign='right',
            valign='middle',
            text_size=self.size)
        self.class_input = TextInput(multiline=False)
        class_box.add_widget(class_label)
        class_box.add_widget(self.class_input)

        level_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        level_label = Label(
            text='Level',
            halign='right',
            valign='middle',
            text_size=self.size)
        self.level_input = TextInput(multiline=False)
        level_box.add_widget(level_label)
        level_box.add_widget(self.level_input)

        gender_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        gender_label = Label(
            text='Gender',
            halign='right',
            valign='middle',
            text_size=self.size)
        self.gender_input = TextInput(multiline=False)
        gender_box.add_widget(gender_label)
        gender_box.add_widget(self.gender_input)

        race_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        race_label = Label(
            text='Race',
            halign='right',
            valign='middle',
            text_size=self.size)
        self.race_input = TextInput(multiline=False)
        race_box.add_widget(race_label)
        race_box.add_widget(self.race_input)

        age_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        age_label = Label(
            text='Age',
            halign='right',
            valign='middle',
            text_size=self.size)
        self.age_input = TextInput(multiline=False)
        age_box.add_widget(age_label)
        age_box.add_widget(self.age_input)

        height_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        height_label = Label(
            text='Height',
            halign='right',
            valign='middle',
            text_size=self.size)
        self.height_input = TextInput(multiline=False)
        height_box.add_widget(height_label)
        height_box.add_widget(self.height_input)

        weight_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        weight_label = Label(
            text='Weight',
            halign='right',
            valign='middle',
            text_size=self.size)
        self.weight_input = TextInput(multiline=False)
        weight_box.add_widget(weight_label)
        weight_box.add_widget(self.weight_input)

        size_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        size_label = Label(
            text='Size',
            halign='right',
            valign='middle',
            text_size=self.size)
        self.size_input = TextInput(multiline=False)
        size_box.add_widget(size_label)
        size_box.add_widget(self.size_input)

        box_1 = BoxLayout(
            orientation='vertical',
            spacing=15)

        box_2 = BoxLayout(
            orientation='vertical',
            spacing=15)

        box_1.add_widget(name_box)
        box_1.add_widget(alignment_box)
        box_1.add_widget(class_box)
        box_1.add_widget(level_box)
        box_1.add_widget(gender_box)
        box_2.add_widget(race_box)
        box_2.add_widget(age_box)
        box_2.add_widget(height_box)
        box_2.add_widget(weight_box)
        box_2.add_widget(size_box)

        top_box = BoxLayout(
            orientation='horizontal',
            size_hint=(.5, .3),
            pos_hint={'center_x': .25, 'center_y': .7})
        top_box.add_widget(box_1)
        top_box.add_widget(box_2)

        content = FloatLayout()
        content.add_widget(Image(
            source='src/images/sheep-knight.png',
            allow_stretch=False,
            keep_ratio=False,
            pos_hint={'center_x': .8, 'center_y': .6}))
        content.add_widget(top_box)

        self.text = 'General'
        self.content = content
