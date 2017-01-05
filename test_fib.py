from fib import *

def test_zero():
	input = 0
	calculated_value = fib(input)
	expected_value = 1
	assert calculated_value == expected_value
	
def test_one():
	input = 0
	calculated_value = fib(input)
	expected_value = 1
	assert calculated_value == expected_value

def test_float():
	input = 3.0
	calculated_value = fib(input)
	expected_value = 3
	assert calculated_value == expected_value
	
#def test_negative():
#	input = -1
#	calculated_value = fib(input)
#	expected_value = -1
#	assert calculated_value == expected_value