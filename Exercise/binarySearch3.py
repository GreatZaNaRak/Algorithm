gg = __import__('sys').stdin
n = gg.readline()
arr = [int(i) for i in gg.readline().split()]
s = set(arr)
d = dict([(j, i) for i, j in enumerate(arr)])
q = [int(i) for i in gg.readline().split()]
for i in q:
    if i < arr[0]: print(-1)
    elif i >= arr[-1]: print(len(arr)-1)
    else:
        temp = i
        while temp not in s:
            temp -=1
        print(d[temp])