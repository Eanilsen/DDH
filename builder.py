from kivy.app import App
#kivy.require("1.9.1")

from random import random
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.button import Button

class DrawInput(Widget):

	def on_touch_down(self, touch):
		print touch
		color = (random(), 1, 1)
		with self.canvas:
			Color(*color, mode='hsv')
			d = 50.0
			Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
			touch.ud["line"] = Line(points=(touch.x, touch.y))
			
	def on_touch_move(self, touch):
		print(touch)
		touch.ud["line"].points += (touch.x, touch.y)
		
	

class HomeScreen(Screen):
	pass
	
	
class HostScreen(Screen):
	pass
	
class ScreenManagement(ScreenManager):
	pass
	
presentation = Builder.load_file("kivy_for_builder.kv")
	
class SimpleKivy (App):

	def clear_canvas(self, obj):
		self.DrawInput.canvas.clear()

	def build(self):
		return presentation
		
if __name__ == "__main__":
	SimpleKivy().run()
	
	
	
	
	
	
	
	
	
	
	