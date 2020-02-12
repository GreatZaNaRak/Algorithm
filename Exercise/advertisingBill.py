gg = __import__('sys').stdin

_ = [int(i) for i in gg.readline().split()]
arr = [int(i) for i in gg.readline().split()]
res = [0]*len(arr)
res[0] = arr[0]
res[1] = max(arr[0], arr[1])

for i in range(2, len(arr)):
    res[i] = max(arr[i]+res[i-2], res[i-1])
print(res[-1])
