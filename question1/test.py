from question1 import *
import pytest

def testswap():
	lst = [1,3,6,7,8]
	assert swap(lst) == [8,3,6,7,1]