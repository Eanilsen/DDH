import random

def die(x, y = 1):  
	
	
	"""Roll the dice 'x' sides and 'y' Times """
	result = []
	for i in range(y):
		result.append(random.randint(1, x))
	return result
	print result 



d20 = die(20, 1)
d6 = die(6, 1)

print """Roll a D20 die and A D6"""
print d20 
print d6

	
