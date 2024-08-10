a = [1,6,9,0,-2]
sus = a[0]
for i in range(1,len(a)):
	if a [i]<sus:
		sus = a[i]
		print("Min element in the list is",sus)