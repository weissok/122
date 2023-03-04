a=[int(x) for x in open('27-B.txt')]  
a.pop(0)
ma=[]
l=len(a)
ser=len(a)//2 
a=a+a
interval = 50000
index = 1000000
mini = 1000000000000000
nach = 0
kon = 1000000
while True:
    mini = 1000000000000000
    for i in range(nach,kon-1,interval):
        d=a[i:i+l]
        kost=0
        for x in range(len(d)):
            if x>ser:
                ind=l-x
            else:
                ind=x
            kost=kost+d[x]*ind
        if mini > kost:
            mini = kost
            index = i
    if interval == 1: 
        exit()
    print(nach+1,kon+1,mini, index)
    
    nach = index - interval
    kon  = index + interval
    interval = interval//10
    if interval == 0: 
        interval = 1
