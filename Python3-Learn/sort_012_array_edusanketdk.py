# AUTHOR: Sanket Khadse
# Python3 Concept: Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
# Github: https://www.github.com/edusanketdk

def sol_1(ar: list) -> list:
    """using count (not inplace)"""
    return [0]*ar.count(0) + [1]*ar.count(1) + [2]*ar.count(2)


def sol_2(ar: list) -> list:
    """using count (inplace)"""
    cnt = [0, 0, 0]
    for i in ar:
        cnt[i] += 1

    for i in range(len(ar)):
        if cnt[0]:
            ar[i] = 0
        elif cnt[1]:
            ar[i] = 1
        else:
            ar[i] = 2

        cnt[ar[i]] -= 1

    return ar


def sol_3(ar: list) -> list:
    """using three pointers"""
    i, l, h = 0, 0, n-1

    while i <= h:
        if arr[i] == 0:
            arr[i], arr[l] = arr[l], arr[i]
            l += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[h] = arr[h], arr[i]
            h -= 1

    return arr