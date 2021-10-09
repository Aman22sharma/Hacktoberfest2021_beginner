# AUTHOR: Sanket Khadse
# Python3 Concept: Find first and last positions of an element in a sorted array
# GITHUB: https://github.com/edusanketdk


def sol_1(ar: list, x: int) -> tuple:
    """using index function"""
    return (ar.index(x), len(ar)-ar[::-1].index(x)-1) if x in ar else (-1, -1)


def sol_2(ar: list, x: int) -> tuple:
    """using single traversal"""
    f, l = -1, -1

    for i in range(len(ar)):
        if ar[i] == x:
            if f == -1: f = i
        l = i

    return (f, l)


def sol_3(ar: list, x: int) -> list:
    """using binary search"""
    ans = [-1, -1]

    l, r = 0, n-1
    while l <= r:
        m = l + (r-l)//2
        if ar[m] == x and (m == 0 or ar[m-1] < x):
            ans[0] = m
            break
        elif ar[m] < x:
            l, r = m+1, r
        else:
            l, r = l, m-1

    l, r = 0, n-1
    while l <= r:
        m = l + (r-l)//2
        if ar[m] == x and (m == n-1 or ar[(m+1)%n] > x):
            ans[1] = m
            break
        elif ar[m] > x:
            l, r = l, m-1
        else:
            l, r = m+1, r

    return ans
