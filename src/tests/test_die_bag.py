from nose.tools import *
from util import die_bag

def test_die_bag_roll():
	"""
	This test looks for the result of a die roll in the function die.
	Tests that the result is inrange for the die roll.  
	"""
	result = die_bag.die(6)
	assert_true(result[0] >= 1 and result[0] <= 6)

def test_die_bag_roll_several_results():
	"""
	This test rool 20 die with 20 eyes. Tests the returned list. For "inrange"
	results.
	"""
	results = die_bag.die(20, 20)
	for result in results:
		assert_true(result >= 1 and result <= 20)