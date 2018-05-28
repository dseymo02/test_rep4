def swap(lst):
	minn = min(lst)
	maxx = max(lst)
	size = len(lst)
	for i in range(0,size):
		if lst[i] == minn:
			lst[i] = maxx
		elif lst[i] == maxx:
			lst[i] = minn
	return lst


