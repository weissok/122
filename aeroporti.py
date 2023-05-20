from itertools import product
import operator
m=[[],
   [712],
   [673,1385],
   [1075,1800,1499],
   [875,1577,239,1287],
   [1622,2348,2046,551,1835],
   [423,1128,244,1266,422,1813]]
wm=0
gr=[]
ways=list(product('0123456', repeat=7))
for x in ways:
    s=[]
    #if all(x.count(a)==1 for a in x):
    if len(set(x))==7:
        for n in range(len(x)-1):
            if int(x[n])<int(x[n+1]):
                s.append(m[int(x[n+1])][int(x[n])])
            else:
                s.append(m[int(x[n])][int(x[n+1])])
    p=[]
    p.append(x)
    p.append(sum(s))
    gr.append(p)
gr.sort(key=operator.itemgetter(1))
print(gr[-1])
