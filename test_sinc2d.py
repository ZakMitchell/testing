from sinc2d import *
import numpy as np

def test_corner():
	inputx = 0
	inputy = 0
	calculated_value = sinc2d(inputx,inputy)
	expected_value = 1
	assert calculated_value == expected_value

def test_edgex():
	inputx = 0
	inputy = 1
	calculated_value = sinc2d(inputx,inputy)
	expected_value = np.sin(inputy) / inputy
	assert calculated_value == expected_value
	
def test_edgey():
	inputx = 1
	inputy = 0
	calculated_value = sinc2d(inputx,inputy)
	expected_value = np.sin(inputx) / inputx
	assert calculated_value == expected_value
	
def test_norm():
	inputx = 0.5
	inputy = 0.5
	calculated_value = sinc2d(inputx,inputy)
	expected_value = (np.sin(inputx) / inputx) * (np.sin(inputy) / inputy)
	assert calculated_value == expected_value