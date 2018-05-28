def printwords(lst):
	size = lst.pop(0)
	listorder = []
	count = 0
	distinct = []
	for index in range(0,size):
		if lst[index] not in distinct:
			distinct.append(lst[index])
	for word in distinct:
		count = lst.count(word)
		listorder.append((word,count))


	return listorder, distinct

