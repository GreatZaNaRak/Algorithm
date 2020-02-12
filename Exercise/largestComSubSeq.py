x=input().strip()
y=input().strip()

st = [[0 for j in range(len(x)+1)] for i in range(len(y)+1)]

for i in range(1, len(y)+1):
    for j in range(1, len(x)+1):
        if x[j-1] == y[i-1]: st[i][j] = st[i-1][j-1] + 1
        elif x[j-1] != y[i-1]: st[i][j] = max(st[i-1][j], st[i][j-1])
print(st[-1][-1])