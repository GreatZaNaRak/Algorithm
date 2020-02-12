gg = __import__('sys').stdin

_, total = [int(i) for i in gg.readline().split()]
coins = sorted([int(i) for i in gg.readline().split()])

arr = [float('inf') for i in range(total+1)]
arr[0] = 0

for i in range(1, len(arr)):
    temp = arr[i]
    for c in coins:
        if c > i: break
        index = i - c
        temp = min(arr[index]+1, temp)
    arr[i] = temp

print(arr[-1])