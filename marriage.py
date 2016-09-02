class Person(object):
	"""docstring for person"""
	def __init__(self):
		self.married = False
		self.married_to = -1
		self.pref_list = []

	def isMarried(self):
		return self.married

	def setMarried(self, val):
		self.married = val

	def get_pref_list(self):
		return self.pref_list

	def set_pref_list(self, arr):
		self.pref_list = arr

	def get_married_to(self):
		return self.married_to

	def set_married_to(self, val):
		self.married_to = val

#Make it dynamic by asking user for value of n
#n = int(raw_input("\nEnter the number of pairs: "))
n = 5
flag = 1

men = []
women = []

for x in range(n):
	men.append(Person())
	women.append(Person())

#allTrue() function checks whether all men are married or not. As the number of men and
#women are equal, all women will also be married when all men are.

def allTrue():
	t_arr = []
	t_var = True
	for x in range(n):
		t_arr.append(men[x].isMarried())

	for x in range(n):
		t_var = t_var and t_arr[x]

	return t_var

print "\nSTABLE MATCHING MARRIAGE PROBLEM"
print "--------------------------------"

#setting prefernces manually. Make it user specific by accepting preference arrays from
#the user and append it to pref_man[] or pref_array[]
#1 in pref_man[] represents woman 1
#1 in pref_woman[] represents man 1
pref_man = []
pref_man.append([2,1,4,5,3])
pref_man.append([4,2,1,3,5])
pref_man.append([2,5,3,4,1])
pref_man.append([1,4,3,2,5])
pref_man.append([2,4,1,5,3])

pref_woman = []
pref_woman.append([5,1,2,4,3])
pref_woman.append([3,2,4,1,5])
pref_woman.append([2,3,4,5,1])
pref_woman.append([1,5,4,3,2])
pref_woman.append([4,2,5,3,1])

for x in range(n):
	men[x].set_pref_list(pref_man[x])
	women[x].set_pref_list(pref_woman[x])

print "\nDisplaying Preference List"
print "--------------------------"

print "\nMen\n---"
for x in range(n):
	print "\nMan ",x+1,": ", men[x].get_pref_list()

print "\nWomen\n-----"
for x in range(n):
	print "\nWoman ",x+1,": ", women[x].get_pref_list()

i = 0

#The logic is that the while loop should function until all get married
while allTrue()==False:
	j = 0
	while j<n and men[i].isMarried() != True:
		if women[men[i].get_pref_list()[j]-1].isMarried() == False:
			men[i].setMarried(True)
			men[i].set_married_to(men[i].get_pref_list()[j]-1)
			women[men[i].get_pref_list()[j]-1].setMarried(True)
			women[men[i].get_pref_list()[j]-1].set_married_to(i)
			
		else:
			if women[men[i].get_pref_list()[j]-1].get_pref_list().index(i+1) < women[men[i].get_pref_list()[j]-1].get_pref_list().index(women[men[i].get_pref_list()[j]-1].get_married_to()+1):
				men[women[men[i].get_pref_list()[j]-1].get_married_to()].setMarried(False)
				k = women[men[i].get_pref_list()[j]-1].get_married_to()
				men[women[men[i].get_pref_list()[j]-1].get_married_to()].set_married_to(-1)
				men[i].setMarried(True)
				men[i].set_married_to(men[i].get_pref_list()[j]-1)
				women[men[i].get_pref_list()[j]-1].setMarried(True)
				women[men[i].get_pref_list()[j]-1].set_married_to(i)
				i = k
				j = -1

			else:
				pass
		j += 1
	i += 1
	if i==5:
		i = 0



print "\nMarried Details"
print "---------------"

for x in range(n):
	print "\nMan ",x+1," married to: Woman ", men[x].get_married_to()+1
