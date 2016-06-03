from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class AttributesTab(TabbedPanelHeader):
    def __init__(self, **kwargs):
        super(AttributesTab, self).__init__(**kwargs)
        strength_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=5)
        strength_label = Label(
            text='Strength',
            size_hint=(.4, 1))
        strength_score = TextInput(multiline=False)
        strength_enh_mod = TextInput(multiline=False)
        strength_misc_mod = TextInput(multiline=False)
        strength_temp_score = Label(text='0', size_hint=(.3, 1))
        strength_box.add_widget(strength_label)
        strength_box.add_widget(strength_score)
        strength_box.add_widget(strength_enh_mod)
        strength_box.add_widget(strength_misc_mod)
        strength_box.add_widget(strength_temp_score)

        dexterity_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=5)
        dexterity_label = Label(
            text='Dexterity',
            size_hint=(.4, 1))
        dexterity_score = TextInput(multiline=False)
        dexterity_enh_mod = TextInput(multiline=False)
        dexterity_misc_mod = TextInput(multiline=False)
        dexterity_temp_score = Label(text='0', size_hint=(.3, 1))
        dexterity_box.add_widget(dexterity_label)
        dexterity_box.add_widget(dexterity_score)
        dexterity_box.add_widget(dexterity_enh_mod)
        dexterity_box.add_widget(dexterity_misc_mod)
        dexterity_box.add_widget(dexterity_temp_score)

        constitution_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=5)
        constitution_label = Label(
            text='Constitution',
            size_hint=(.4, 1))
        constitution_score = TextInput(multiline=False)
        constitution_enh_mod = TextInput(multiline=False)
        constitution_misc_mod = TextInput(multiline=False)
        constitution_temp_score = Label(text='0', size_hint=(.3, 1))
        constitution_box.add_widget(constitution_label)
        constitution_box.add_widget(constitution_score)
        constitution_box.add_widget(constitution_enh_mod)
        constitution_box.add_widget(constitution_misc_mod)
        constitution_box.add_widget(constitution_temp_score)

        intelligence_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=5)
        intelligence_label = Label(
            text='Intelligence',
            size_hint=(.4, 1))
        intelligence_score = TextInput(multiline=False)
        intelligence_enh_mod = TextInput(multiline=False)
        intelligence_misc_mod = TextInput(multiline=False)
        intelligence_temp_score = Label(text='0', size_hint=(.3, 1))
        intelligence_box.add_widget(intelligence_label)
        intelligence_box.add_widget(intelligence_score)
        intelligence_box.add_widget(intelligence_enh_mod)
        intelligence_box.add_widget(intelligence_misc_mod)
        intelligence_box.add_widget(intelligence_temp_score)

        wisdom_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=5)
        wisdom_label = Label(
            text='Wisdom',
            size_hint=(.4, 1))
        wisdom_score = TextInput(multiline=False)
        wisdom_enh_mod = TextInput(multiline=False)
        wisdom_misc_mod = TextInput(multiline=False)
        wisdom_temp_score = Label(text='0', size_hint=(.3, 1))
        wisdom_box.add_widget(wisdom_label)
        wisdom_box.add_widget(wisdom_score)
        wisdom_box.add_widget(wisdom_enh_mod)
        wisdom_box.add_widget(wisdom_misc_mod)
        wisdom_box.add_widget(wisdom_temp_score)

        charisma_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=5)
        charisma_label = Label(
            text='Charisma',
            size_hint=(.4, 1))
        charisma_score = TextInput(multiline=False)
        charisma_enh_mod = TextInput(multiline=False)
        charisma_misc_mod = TextInput(multiline=False)
        charisma_temp_score = Label(text='0', size_hint=(.3, 1))
        charisma_box.add_widget(charisma_label)
        charisma_box.add_widget(charisma_score)
        charisma_box.add_widget(charisma_enh_mod)
        charisma_box.add_widget(charisma_misc_mod)
        charisma_box.add_widget(charisma_temp_score)

        ability_score_box= BoxLayout(
            orientation='vertical',
            size_hint=(.35, .3),
            pos_hint={'center_x': .28, 'center_y': .725})

        ability_score_box.add_widget(strength_box)
        ability_score_box.add_widget(dexterity_box)
        ability_score_box.add_widget(constitution_box)
        ability_score_box.add_widget(intelligence_box)
        ability_score_box.add_widget(wisdom_box)
        ability_score_box.add_widget(charisma_box)

        ability_score_names = BoxLayout(
            orientation='horizontal',
            pos_hint={'center_x': .25, 'center_y': .9},
            size_hint=(.40, .5),
            spacing=100)
        ability_score_names.add_widget(Label(text='Ability'))
        ability_score_names.add_widget(Label(text='Score'))
        ability_score_names.add_widget(Label(text='Enh Mod'))
        ability_score_names.add_widget(Label(text='Misc Mod'))
        ability_score_names.add_widget(Label(text='Temp Score'))

        hp_box = BoxLayout(
            orientation='horizontal',
            size_hint=(.6, .25),
            pos_hint={'center_x': .25, 'center_y': .55},
            spacing=5)
        hp_label = Label(
            text='HP',
            size_hint=(.8, .2),
            text_size=self.size,
            halign='right',
            valign='middle')
        hp_total = TextInput(multiline=False, size_hint=(.8, .2))
        hp_current = TextInput(multiline=False, size_hint=(.8, .2))
        hp_current = TextInput(multiline=False, size_hint=(.8, .2))
        hp_non_lethal_damage = TextInput(multiline=False, size_hint=(.8, .2))
        hp_hit_dice = TextInput(multiline=False, size_hint=(.8, .2))
        hp_damage_reduction = TextInput(multiline=False, size_hint=(.8, .2))

        hp_box.add_widget(hp_label)
        hp_box.add_widget(hp_total)
        hp_box.add_widget(hp_current)
        hp_box.add_widget(hp_non_lethal_damage)
        hp_box.add_widget(hp_hit_dice)
        hp_box.add_widget(hp_damage_reduction)

        hp_names = BoxLayout(
            orientation='horizontal',
            pos_hint={'center_x': .3, 'center_y': .5},
            size_hint=(.5, .5),
            spacing=5)
        hp_names.add_widget(Label(text='Total'))
        hp_names.add_widget(Label(text='Current HP'))
        hp_names.add_widget(Label(text='Nonlethal Damage'))
        hp_names.add_widget(Label(text='Hit Dice'))
        hp_names.add_widget(Label(text='Damage Reduction'))

        ac_box = BoxLayout(
            orientation='horizontal',
            size_hint=(.6, .25),
            pos_hint={'center_x': .29, 'center_y': .45})
        ac_label = Label(
            text='AC',
            size_hint=(.8, .2),
            text_size=self.size,
            halign='center',
            valign='middle')
        ac_total = TextInput(multiline=False, size_hint=(.8, .2))
        ac_armor = TextInput(multiline=False, size_hint=(.8, .2))
        ac_sheild = TextInput(multiline=False, size_hint=(.8, .2))
        ac_mod = TextInput(multiline=False, size_hint=(.8, .2))
        ac_size = TextInput(multiline=False, size_hint=(.8, .2))
        ac_deflect = TextInput(multiline=False, size_hint=(.8, .2))
        ac_natural = TextInput(multiline=False, size_hint=(.8, .2))
        ac_dodge = TextInput(multiline=False, size_hint=(.8, .2))
        ac_misc = TextInput(multiline=False, size_hint=(.8, .2))
        ac_box.add_widget(ac_label)
        ac_box.add_widget(ac_total)
        ac_box.add_widget(ac_armor)
        ac_box.add_widget(ac_sheild)
        ac_box.add_widget(ac_mod)
        ac_box.add_widget(ac_size)
        ac_box.add_widget(ac_deflect)
        ac_box.add_widget(ac_natural)
        ac_box.add_widget(ac_dodge)
        ac_box.add_widget(ac_misc)

        ac_names = BoxLayout(
            orientation='horizontal',
            pos_hint={'center_x': .31, 'center_y': .4},
            size_hint=(.55, .5))
        ac_names.add_widget(Label(text='Total'))
        ac_names.add_widget(Label(text='Armor'))
        ac_names.add_widget(Label(text='Shield'))
        ac_names.add_widget(Label(text='Mod'))
        ac_names.add_widget(Label(text='Size'))
        ac_names.add_widget(Label(text='Deflect'))
        ac_names.add_widget(Label(text='Natural'))
        ac_names.add_widget(Label(text='Dodge'))
        ac_names.add_widget(Label(text='Misc'))

        initiative_box = BoxLayout(
            orientation='horizontal',
            size_hint=(.3, .25),
            pos_hint={'center_x': .15, 'center_y': .33})
        initiative_label = Label(
            text='Initiative',
            size_hint=(.8, .2),
            text_size=self.size,
            halign='center',
            valign='middle')
        initiative_total = TextInput(multiline=False, size_hint=(.8, .2))
        initiative_dex = TextInput(multiline=False, size_hint=(.8, .2))
        initiative_misc = TextInput(multiline=False, size_hint=(.8, .2))
        initiative_speed = TextInput(multiline=False, size_hint=(.8, .2))
        initiative_armor_type = TextInput(multiline=False, size_hint=(.8, .2))
        initiative_box.add_widget(initiative_label)
        initiative_box.add_widget(initiative_total)
        initiative_box.add_widget(initiative_dex)
        initiative_box.add_widget(initiative_misc)
        initiative_box.add_widget(initiative_speed)
        initiative_box.add_widget(initiative_armor_type)

        initiative_names = BoxLayout(
            orientation='horizontal',
            pos_hint={'center_x': .17, 'center_y': .28},
            size_hint=(.26, .5))
        initiative_names.add_widget(Label(text='Total'))
        initiative_names.add_widget(Label(text='Dex'))
        initiative_names.add_widget(Label(text='Misc'))
        initiative_names.add_widget(Label(text='Speed'))
        initiative_names.add_widget(Label(text='Armor Type'))

        fortitude_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1.5, .2),
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=5)
        fortitude_label = Label(
            text='Fortitude',
            size_hint=(.8, .2),
            text_size=self.size,
            halign='center',
            valign='middle')
        fortitude_total = TextInput(multiline=False, size_hint=(.8, .4))
        fortitude_base = TextInput(multiline=False, size_hint=(.8, .4))
        fortitude_ability_mod = TextInput(multiline=False, size_hint=(.8, .4))
        fortitude_magic_mod = TextInput(multiline=False, size_hint=(.8, .4))
        fortitude_misc_mod = TextInput(multiline=False, size_hint=(.8, .4))
        fortitude_temp = TextInput(multiline=False, size_hint=(.8, .4))
        fortitude_box.add_widget(fortitude_label)
        fortitude_box.add_widget(fortitude_total)
        fortitude_box.add_widget(fortitude_base)
        fortitude_box.add_widget(fortitude_ability_mod)
        fortitude_box.add_widget(fortitude_magic_mod)
        fortitude_box.add_widget(fortitude_misc_mod)
        fortitude_box.add_widget(fortitude_temp)

        reflex_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1.5, .2),
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=5)
        reflex_label = Label(
            text='Reflex',
            size_hint=(.8, .4),
            text_size=self.size,
            halign='center',
            valign='middle')
        reflex_total = TextInput(multiline=False, size_hint=(.8, .4))
        reflex_base = TextInput(multiline=False, size_hint=(.8, .4))
        reflex_ability_mod = TextInput(multiline=False, size_hint=(.8, .4))
        reflex_magic_mod = TextInput(multiline=False, size_hint=(.8, .4))
        reflex_misc_mod = TextInput(multiline=False, size_hint=(.8, .4))
        reflex_temp = TextInput(multiline=False, size_hint=(.8, .4))
        reflex_box.add_widget(reflex_label)
        reflex_box.add_widget(reflex_total)
        reflex_box.add_widget(reflex_base)
        reflex_box.add_widget(reflex_ability_mod)
        reflex_box.add_widget(reflex_magic_mod)
        reflex_box.add_widget(reflex_misc_mod)
        reflex_box.add_widget(reflex_temp)

        will_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1.5, .2),
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=5)
        will_label = Label(
            text='Will',
            size_hint=(.8, .4),
            text_size=self.size,
            halign='center',
            valign='middle')
        will_total = TextInput(multiline=False, size_hint=(.8, .4))
        will_base = TextInput(multiline=False, size_hint=(.8, .4))
        will_ability_mod = TextInput(multiline=False, size_hint=(.8, .4))
        will_magic_mod = TextInput(multiline=False, size_hint=(.8, .4))
        will_misc_mod = TextInput(multiline=False, size_hint=(.8, .4))
        will_temp = TextInput(multiline=False, size_hint=(.8, .4))
        will_box.add_widget(will_label)
        will_box.add_widget(will_total)
        will_box.add_widget(will_base)
        will_box.add_widget(will_ability_mod)
        will_box.add_widget(will_magic_mod)
        will_box.add_widget(will_misc_mod)
        will_box.add_widget(will_temp)

        saving_throws_box = BoxLayout(
            orientation='vertical',
            size_hint=(.3, .4),
            pos_hint={'center_x': .77, 'center_y': .75})
        saving_throws_box.add_widget(fortitude_box)
        saving_throws_box.add_widget(reflex_box)
        saving_throws_box.add_widget(will_box)

        base_attack_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        base_attack_label = Label(text='Base Attack')
        base_attack_input = TextInput(multiline=False)
        base_attack_box.add_widget(base_attack_label)
        base_attack_box.add_widget(base_attack_input)

        cmb_box = BoxLayout(
            orientation='horizontal',
            size_hint=(.2, .25),
            pos_hint={'center_x': .8, 'center_y': .5})
        cmb_label = Label(
            text='CMB',
            size_hint=(.1, .2),
            text_size=self.size,
            halign='center',
            valign='middle')
        cmb_input = TextInput(multiline=False, size_hint=(.1, .2))
        cmb_box.add_widget(cmb_label)
        cmb_box.add_widget(cmb_input)

        cmd_box = BoxLayout(
            orientation='horizontal',
            size_hint=(.2, .25),
            pos_hint={'center_x': .8, 'center_y': .4})
        cmd_label = Label(
            text='CMD',
            size_hint=(.1, .2),
            text_size=self.size,
            halign='center',
            valign='middle')
        cmd_input = TextInput(multiline=False, size_hint=(.1, .2))
        cmd_box.add_widget(cmd_label)
        cmd_box.add_widget(cmd_input)

        content = FloatLayout()
        content.add_widget(ability_score_box)
        content.add_widget(ability_score_names)
        content.add_widget(hp_box)
        content.add_widget(hp_names)
        content.add_widget(ac_box)
        content.add_widget(ac_names)
        content.add_widget(saving_throws_box)
        content.add_widget(initiative_box)
        content.add_widget(initiative_names)
        content.add_widget(cmd_box)
        content.add_widget(cmb_box)
        
        self.content = content
        self.text='Attributes'
