def gcd(n1: int, n2: int):
#     *METHOD :1* T.C. = O(N^2), S.C. = O(N)
#     s1 = set()
#     s2 = set()
    # for i in range(1, n1+1):
    #     if n1 % i == 0:
    #         s1.add(i)
    # for i in range(1, n2+1):
    #     if n2 % i == 0:
    #         s2.add(i)
    # new_values = s1.intersection(s2)
    # return max(new_values)
    # if n1 == 0:
    #     return n2
    # return gcd(n2 % n1, n1)
    
#    *METHOD: 2*, T.C. = O(N), S.C. = O(1)
#     val = 0
#     if n1 > n2:
#         small = n2
#     else:
#         small = n1
#     for i in range(1,small+1):
#         if n1 % i == 0 and n2 % i == 0:
#             val = i
#     return val
# METHOD 3: Eucledian Algorithm O(n)->T.C., space complexity = O(1)
    if n1 == 0:
        return n2
    return gcd(n2 % n1, n1)


def lcm(a, b):
    prod = a*b
    g = gcd(a, b)
    return prod // g


print("Gcd is ", gcd(60, 48))
print("lcm is ", lcm(20, 50))
