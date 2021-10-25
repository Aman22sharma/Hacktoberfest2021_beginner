from array import array
arr=array("i",[1,2,3,3,4,5,5,5,6,7])
num=3
low=0
high=len(arr)-1
while low<=high:
	mid=int((low+high)/2)
	if arr[mid]==3 and arr[mid-1]<3:
		print("First index: ",mid)
		low=mid+1
	elif arr[mid]==3 and arr[mid+1]>3:
		print("Last index: ",mid)
		high=mid-1
	if arr[mid]<3:
		low=mid+1
	elif arr[mid]>3:
		high=mid-1