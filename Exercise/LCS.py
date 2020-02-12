x, y = input("enter >> ").split()

def LCS(x, y, i, j):
    nx = x[0:i]
    ny = y[0:j]
    if len(nx) == 0 or len(ny) == 0: return 0
    if nx[-1] == ny[-1]: return LCS(nx, ny, i-1, j-1) + 1
    return max(LCS(nx, ny, i-1, j), LCS(nx, ny, i, j-1))

#  -------------- divide and conquer method ---------------------------  #

st = [[0 for j in range(len(x)+1)] for i in range(len(y)+1)]

def LCS2(x, y, i, j, st):
    nx = x[0:i]
    ny = y[0:j]
    if len(nx) == 0 or len(ny) == 0: return 0
    if st[i-1][j-1] != 0: return st[i-1][j-1]
    if nx[-1] == ny[-1]:
        st[i-1][j-1] = LCS2(nx, ny, i-1, j-1, st) + 1 # add memoization
        return st[i-1][j-1]
    st[i-1][j-1] = max(LCS2(nx, ny, i, j-1, st), LCS2(nx, ny, i-1, j, st)) # add memoization
    return st[i-1][j-1]

#  -------------- with top down (memoization) ---------------------------  #

st2 = [[0 for i in range(len(x)+1)] for j in range(len(y)+1)]

def LCS3(x, y, endx, endy, st2):
    for i in range(1, endy+1):
        for j in range(1, endx+1):
            if x[j-1] == y[i-1]: st2[i][j] = st2[i-1][j-1] + 1
            elif x[j-1] != y[i-1]: st2[i][j] = max(st2[i-1][j], st2[i][j-1])
    return st2



#  -------------- with buttom up ------------ ---------------------------  #

print(LCS(x, y, len(x), len(y)))
print(LCS2(x, y, len(y)+1, len(x)+1, st))
a = LCS3(x, y, len(x), len(y), st2)
print(a[-1][-1])