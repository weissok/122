array = [int(x) for x in range(100,201)]
array = array[::-1]
array.append(105)
array.append(110)

r=len(array)
l = 0
lens = len(array)
while lens>2:
    
    lens = len(array)//2
    if array[lens+1]<array[lens]:
        l = lens
    else:
        r = lens  
    if r>l:
        array = array[l:r]   
    
        
print(min(array))
