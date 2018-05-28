def lexorder(lst):
	pass

def distinct(lst,size):
	distinct = []
	for index in range(0,size):
		if lst[index] not in distinct:
			distinct.append(lst[index])
	return distinct

def counting(distinct,lst):
	listorder = []
	for word in distinct:
		count = lst.count(word)
		listorder.append((word,count))
	return listorder

def printwords(lst):
	size = lst.pop(0)
	listorder = []
	count = 0
	dist = distinct(lst,size)
	listorder = counting(dist,lst)
	sortlist = sorted(listorder,key=lambda tup:tup[1],reverse=True)
	finallist = []
	for word in sortlist:
		finallist.append(word[0])
	return finallist


