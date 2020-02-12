gg = __import__('sys').stdin

_ = gg.readline()
p = [int(i) for i in gg.readline().split()]
m = [[0 for i in range(len(p)-1)] for i in range(len(p)-1)]

for i in range(1, len(p)-1):
    for j in range(0, len(p)-1-i):
        k = i + j
        m[j][k] = float('inf')
        for g in range(j, k):
            m[j][k] = min(m[j][k], m[j][g] + m[g+1][k] + p[j-1]*p[g]*p[k])

print(m[0][-1])