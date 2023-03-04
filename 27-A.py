a=[int(x) for x in open('27-A.txt')]  
a.pop(0)
ma=[]
l=len(a)
ser=len(a)//2 
a=a+a
for i in range(l):
    d=a[i:i+l]
    kost=0
    print(d)
    for x in range(len(d)):
        if x>ser:
            ind=l-x
        else:
            ind=x
        kost=kost+d[x]*ind
    ma.append(kost)
    print(kost)

print(ma.index(min(ma))+1)
