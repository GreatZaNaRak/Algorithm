def tile(lr, hr, lc, hc, y, x):
 
    

    if hr - lr == 1: #base case

        if x == lr and y == lc: print(0, lc, lr)
        elif x == lr and y == hc: print(1, lc, lr)
        elif x == hr and y == lc: print(2, lc, lr)
        else: print(3, lc, lr)
        return
    

    mc = (lc + hc) // 2 # นอน
    mr = (lr + hr) // 2 # ตั้ง


    if x <= mr and y <= mc:

        print(0, mc, mr)
        tile(lr, mr, lc, mc, y, x)
        tile(lr, mr, mc+1, hc, mc+1, mr)
        tile(mr+1, hr, mc+1, hc, mc+1, mr+1)
        tile(mr+1, hr, lc, mc, mc, mr+1) 
    

    elif x <= mr and y > mc:
        
        print(1, mc, mr)
        tile(lr, mr, lc, mc, mc, mr)
        tile(lr, mr, mc+1, hc, y, x)
        tile(mr+1, hr, mc+1, hc, mc+1, mr+1)
        tile(mr+1, hr, lc, mc, mc, mr+1) 
        

    elif x > mr and y <= mc:
        
        print(2, mc, mr)
        tile(lr, mr, lc, mc, mc, mr)
        tile(lr, mr, mc+1, hc, mc+1, mr)
        tile(mr+1, hr, mc+1, hc, mc+1, mr+1)
        tile(mr+1, hr, lc, mc, y, x) 
         

    elif x > mr and y > mc:
       # print('down right')
        print(3, mc, mr)
        tile(lr, mr, lc, mc, mc, mr)
        tile(lr, mr, mc+1, hc, mc+1, mr)
        tile(mr+1, hr, mc+1, hc, y, x)
        tile(mr+1, hr, lc, mc, mc, mr+1) 



n, x, y = [int(i) for i in input().split()]
print((n**2 - 1) // 3)
tile(0, n-1, 0, n-1, x, y)