# Selection sort

arr = [64, 25, 12, 22, 11]

for i in range(len(arr)):
	min_idx = i
	for j in range(i+1, len(arr)):
		if arr[min_idx] > arr[j]:
			min_idx = j
	arr[i], arr[min_idx] = arr[min_idx], arr[i]

print("Sorted array:\n",arr)