def next_permuation(arr: list):
    i = j = len(arr) - 1
    while i > 0 and arr[i] <= arr[i-1]:
        i -= 1
    if i == 0:
        return arr.reverse()
    pivot = i - 1
    while arr[pivot] >= arr[j]:
        j -= 1
    arr[pivot], arr[j] = arr[j], arr[pivot]
    print(arr[j])
    print(arr)
    print("pivot is", pivot)
    l1 = pivot + 1
    r = len(arr) - 1
    while l1 < r:
        arr[l1], arr[r] = arr[r], arr[l1]
        l1 += 1
        r -= 1

    print(arr)


A = [0, 1, 2, 5, 3, 3, 0]
print(next_permuation(A))
