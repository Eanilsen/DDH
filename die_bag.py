import random
class die_bag():#Class for rolling die/dices
	
	def __init__(self):
		self.data = []
	
	
	def die(self, x, y = 1):#Roll a die and returns result
		result = []
		for i in range(y):
			result.append(random.randint(1, x))
		return result
		print result 

	
	

	def take_input_die(self):#Take input from user 
	
		eyes = int(raw_input('Number of eyes? '))
		times = int(raw_input('Number of times? '))
		
		#Call die
		dieRoll = die_bag.die(self, eyes, times)
		print dieRoll

d_class = die_bag()#Create a instance of die_bag

die_bag.take_input_die(d_class)#Call take_input_die

#Why does this not work?
die_bag.die(d_class, 20, 1)#Call die with parameters