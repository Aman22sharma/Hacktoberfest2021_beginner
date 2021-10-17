def SelectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [2, 16, 0, -5, 11, -9]
size = len(data)
print('Given Array:')
print(data)
SelectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
