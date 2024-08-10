# name = input("Enter Your Name :- ")
# age = int(input("Enter Your Age :- "))
# if age<18:
# 	print(name,"is a Child")
# elif age==18:
# 	print(name,"is a Teen")
# else:
# 	print(name,"is a Old Person")

# x = int(input("Enter No. : "))

# if x % 2 == 0:
# 	print(x,"Is Even Number")
# else:
# 	print(x, "Is Odd Number")

num = int(input("Enter No. : "))

if num > 1:
	
	for i in range(2, int(num/2)+1):
		
		if (num % i) == 0:
			print(num, "is not a prime number")
			break
	else:
		print(num, "is a prime number")
else:
	print(num, "is not a prime number")
