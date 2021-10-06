# AUTHOR: Sanket Khadse
# Python3 Concept: Find Duplicate characters in a string
# GITHUB: https://github.com/edusanketdk

def sol_1(s: str) -> dict:
    """using default dictionary"""
    from collections import defaultdict

    dct = defaultdict(int)
    for i in s:
        dct[i] += 1

    ans = dict()
    for i in dct:
        if dct[i] > 1:
            ans[i] = dct[i]

    return ans

def sol_2(s: str) -> dict:
    """using ascii array"""
    ar = [0]*26
    for i in s:
        ar[ord(i)-97] += 1

    ans = {}
    for i in range(26):
        if ar[i] > 1:
            ans[chr(97+i)] = ans[i]

    return ans
