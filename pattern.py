#Hollow Triangle
'''a = int(input("Enter No. "))
px = a
py = a
for x in range(1,a+1):
	for y in range(1,a*2):
		if(y == px or y == py or x == a):
			print("*" ,end=" ")
		else:
			print(" ",end=" ")
	px -= 1
	py += 1
	print( )'''
	
#Hollow Heart
#a = int(input("Enter First No. "))
#b = int(input("Enter Second No. "))
'''for row in range(0,6):
	for col in range(0,7):
		if(row == 0 and col % 3 != 0) or (row ==1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print("")'''