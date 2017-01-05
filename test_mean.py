from mean import *

def test_ints():
	input = [1,2,3,4,5]
	calculated_value = mean(input)
	expected_value = 3
	assert calculated_value == expected_value

def test_float():
	input = [1.5,2.5,3.5,4.5,5.5]
	calculated_value = mean(input)
	expected_value = 3.5
	assert calculated_value == expected_value
	
def test_zero():
	input = [0,0,0,0,0]
	calculated_value = mean(input)
	expected_value = 0
	assert calculated_value == expected_value
	
#def test_string():
#	input = "Hello"
#	calculated_value = mean(input)
#	expected_value = 0
#	assert calculated_value == expected_value
	
#def test_badtest():
#	input = [0,1,2,3,4]
#	calculated_value = mean(input)
#	expected_value = 0
#	assert calculated_value == expected_value