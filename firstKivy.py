import kivy
kivy.require('1.9.1') #current version

from kivy.app import App
from kivy.uix.label import Label

class firstApp(App):
    
    def build(self):
        return Label(text='What do you want to do?')
        
        
    
        
if __name__ == '__main__':
    firstApp().run()
    
    