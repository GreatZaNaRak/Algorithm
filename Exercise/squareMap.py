gg = __import__('sys').stdin

r, c = [int(i) for i in gg.readline().split()]
st = []
m = []

for i in range(r):
    a = [int(i) for i in gg.readline().strip()]
    b = a.copy()
    st.append(a)
    m.append(b)

for i in range(1, r):
    for j in range(1, c):
        if st[i][j] == 1:
            m[i][j] = 1 + min(m[i-1][j-1], m[i-1][j], m[i][j-1])
        else:
            m[i][j] = 0
       
print(max([max(i) for i in m])) # whyyy????