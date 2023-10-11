nr=int(input("Cate numere sunt in lista:"))
contor=1
a=int(input())
min=a
max=a

while contor<nr:
    a=int(input())
    if max<a:
        max=a
    if min>a:
        min=a
    contor+=1

print("Max:",max)
print("Min:",min)