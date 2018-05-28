def power(a,n):
	if n == 0 and a > 0:
		return 1
	elif n in [1,0]:
		return a
	else:
		return a * power(a,n-1)