import sys as s
kb = s.stdin

def merge(data, temp, start, mid, end):
  # res = [0]*len(data) ตอนแรกมีตัวนี้เสียเวลามากๆ
    i = start
    j = mid + 1
    c = 0
    for k in range(start, end+1):
        if i > mid:
            temp[k] = data[j]
            j+=1
            continue
        elif j > end:
            temp[k] = data[i]
            i += 1
            continue
        elif data[i] < data[j]:
            temp[k] = data[i]
            i += 1
        elif data[i] > data[j]:
            temp[k] = data[j]
            c += (mid-i+1)
            j += 1
        else:
            temp[k] = data[i]
            i += 1
        
    for k in range(start, end+1): data[k] = temp[k]
    return c


def mergeSort(data, temp, left, right):
    c = 0
    if left >= right: return 0
    mid = (left+right)//2
    c = mergeSort(data, temp, left, mid)
    c += mergeSort(data, temp, mid+1, right)
    c += merge(data, temp, left, mid, right)
    return c

input()
d = [int(i) for i in kb.readline().split()]
res = [0]*len(d)
print(mergeSort(d, res,  0, len(d)-1))