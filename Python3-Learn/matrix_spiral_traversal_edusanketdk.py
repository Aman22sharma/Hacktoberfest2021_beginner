// AUTHOR: Sanket Khadse
// Python3 Concept: Spirally traversing a matrix
// GITHUB: https://github.com/edusanketdk

def sol_1(mat: list) -> list:
    u, r, d, l, dir = 0, len(mat[0]), len(mat), 0, 0
    ans = []

    while u <= d and l <= r:
        if dir == 0:
            for i in range(l, r+1):
                ans.append(mat[u][i])
            u += 1
        elif dir == 1:
            for i in range(u, d+1):
                ans.append(mat[i][r])
            r -= 1
        elif dir == 2:
            for i in range(r, l-1, -1):
                ans.append(mat[d][i])
            d -= 1
        else:
            for i in range(d, u-1, -1):
                ans.append(mat[i][l])
            l += 1
        dir = (dir + 1)%4

    return ans
