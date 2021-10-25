from array import array
arr=array("i",[3,4,7,5,9,2,1])
sum=int(input("Enter sum number: "))
for i in range(len(arr)):
	for j in range(i+1,len(arr)):
		if sum==arr[i]+arr[j]:
			print(sum," is the sum of ",i," and ",j)