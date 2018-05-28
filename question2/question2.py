def power(a,n):
	if n in [1,0]:
		return a
	else:
		return a * power(a,n-1)