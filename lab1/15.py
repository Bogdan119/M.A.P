a=[]
nr=8
contor=1
true=1
while contor<=8:
    x=int(input("Nr:"))
    a.append(x)
    contor+=1


while true==1:
    true=0
    for i in range(7):
         j=i+1
         if a[i]>a[j]:
            aux=a[i]
            a[i]=a[j]
            a[j]=aux
            true=1

for i in range(8):
   print(a[i])
    