chisla='0123456789'
chisla_spisok=list(chisla)
print(chisla_spisok)
haming='0000000 0001111 0011001 0100101 0101010 0110011 0111100 1000011 1001100'				
haming_spisok=haming.split()
print(haming_spisok)
def distance(x,y):
    k=7
    for i in range(1.7):
        if x%10==y%10:
            k=k-1
            x=x//10
            y=y//10
    return k
cod=int(input("код="))
min=distance(cod,int(haming_spisok[0]))
imin=0
for i in range(1,9):
    D=distance(cod,int(haming_spisok[i]))
    if D<min:
        min=D
        imin=i
print(min)
if min==0:
    print(f"код верный: стмвол {chisla_spisok[min]}")
elif min==1:
    print(f"код исправлен: стмвол {chisla_spisok[min]}")
else:
    print("код неверный")

