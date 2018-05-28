import pytest
from question3 import *

def testlexorder():
	l1 = [('tree',2),('bug',2)]
	assert lexoder(l1) == [('bug',2),('tree',2)]

def testprintwords():
	lst = [3, 'tree','bug','tree']
	assert printwords(lst) == ['tree','bug']

	lst1 = [4,'tree', 'tree','bug', 'bug']
	assert printwords(lst1) == ['bug','tree']
