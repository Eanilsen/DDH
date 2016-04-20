import random

"""In this module, die or dices are rolled"""

def die(x, y = 1):
    """Function for rolling a die or several dice,
    returns an array with results of dice rolls.
    Parameter x is number of eyes on a die.
    Parameter y = 1 is the times to a die is rolled.
    """
    
    result = []
    for i in range(y):
        result.append(random.randint(1, x))
    return result