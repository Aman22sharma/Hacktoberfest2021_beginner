num=int(input("Enter a number: "))
for i in range(2,num+1):
	check=True
	while check:
		if num%i==0:
			print(i)
			num/=i
		else:
			check=False