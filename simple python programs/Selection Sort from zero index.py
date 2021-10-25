from array import array
arr=array('i',[3,5,1,8,4])
length=0
k=0
for i in range(len(arr)):
	se=arr[len(arr)-1]
	index=len(arr)-1
	for j in range(k,len(arr)):
		if se>arr[j]:
			se=arr[j]
			index=j
	arr[length],arr[index]=arr[index],arr[length]
	length+=1
	k+=1
print(arr)