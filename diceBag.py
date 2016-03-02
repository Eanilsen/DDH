#Rolls a die or several dice. 
#Function calling must supply bonuses/penalties 
import random


		
		
		

def die(x, y=1):  
	"""Roll the dice 'x' sides and 'y' Times """
	result = []
	for i in range(y):
		result.append(random.random(1, x))
	return result
	print result 

print """Roll a D20 die"""
die(x = 20,y = 1)
print result
	
	
	
a = 1 
b = 2 
c = a + b 
	
print c	

	
	
	
