gg = __import__('sys').stdin

st = [[int(i) for i in input().split()] for i in range(int(gg.readline()))]

for i in range(len(st)-2, -1, -1):
    for j in range(len(st[i])):
        st[i][j] += max(st[i+1][j], st[i+1][j+1])
        
print(st[0][0])