gg = __import__('sys').stdin

def maxCross(data, left, mid, right):
    tempL = resL = data[mid];
    tempR = resR = data[mid+1];
    for i in range(mid+2, right+1):
        resR += data[i]
        if resR > tempR: tempR = resR
    for i in range(mid-1, left-1, -1): # เปลี่ยนจากถึง 0 เป็นถึง left
        resL += data[i]
        if resL > tempL: tempL = resL
    return tempL + tempR
    
def maxSub(data, left, right):
    if right == left: return data[left]
    mid = (left+right) // 2
    L = maxSub(data, left, mid)
    C = maxCross(data, left, mid, right)
    R = maxSub(data, mid+1, right)
    return max(L, C, R)

input(); res=[int(i) for i in gg.readline().split()]
print(maxSub(res, 0, len(res)-1))