def allLang(num,stud1,stud2):
	stud1.pop(0)
	stud2.pop(0)
	set1 = set(stud1)
	set2 = set(stud2)
	inter = set1 | set2
	newlist = list(inter)
	newlist.sort(reverse=False)
	count = len(inter)
	return count,newlist

def oneLang(num,stud1,stud2):
	stud1.pop(0)
	stud2.pop(0)
	newlist = stud2+stud1
	count = len(newlist)
	newlist2 = list(set(newlist))
	newlist2.sort(reverse=False)
	return count, newlist2

def main():
	num = input("please enter number of students: ")
	students = []
	for n in range(0,num):
		student[n] = input()
	for n in range(0,num):
		resultall = allLang(student[n])




if __name__ == "__main__":
	main()

