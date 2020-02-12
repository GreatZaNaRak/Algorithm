gg = __import__('sys').stdin
n, k = [int(i) for i in gg.readline().split()]

st = [[0 for i in range(n+1)] for i in range(k+1)]
for i in range(n+1):
    st[0][i] = 1

for i in range(k+1):
    for j in range(n+1):
        if i == j: st[i][j] = 1
t = 2
for i in range(1, k+1):
    for j in range(t, n+1):
        st[i][j] = st[i-1][j-1] + st[i][j-1]
    t += 1

print(st[-1][-1])
       