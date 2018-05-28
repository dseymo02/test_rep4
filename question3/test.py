import pytest
from question3 import *

def testprintwords():
	lst = [3, 'tree','bug','tree']
	assert printwords(lst) == ['tree','bug']

	lst1 = [4,'tree', 'tree','bug', 'bug']
	assert printwords(lst1) == ['bug','tree']
