from question4 import *
import pytest

def testAllLang():
	num = 2
	stud1 = [2, 'german','english']
	stud2 = [2, 'english', 'spanish']
	assert allLang(num, stud1,stud2) == (3,['english','german','spanish'])

def testOneLang():
	num = 2
	stud1 = [2, 'german','english']
	stud2 = [2, 'english', 'spanish']
	assert oneLang(num, stud1,stud2) == (4,['english','german','spanish'])
