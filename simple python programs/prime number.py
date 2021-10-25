num=int(input("Enter a number: "))
check=False
for i in range(2,13):
	if num%i==0:
		check=True
		print("Number is not prime")
		break
else:
	print("Number is prime")