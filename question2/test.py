from question2 import *
import pytest

def testpower():
	a = 2
	n = 2
	assert power(a,n) == 4

	a1 = 0
	n1 = 0
	assert power(a1,n1) == 0