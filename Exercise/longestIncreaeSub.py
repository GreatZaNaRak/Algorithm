gg = __import__('sys').stdin

gg.readline()
a = [int(i) for i in gg.readline().split()]
b = [1]*len(a)

for i in range(1, len(a)):
    for j in range(i):
        if a[i] > a[j]:
            b[i] = max(b[j]+1, b[i])
print(max(b))