a=int(input("Da=ti nr:"))
d=1
check=1

for d in range(2,a):
    if (a%d)==0:
        check=0

if check==1:
    print("NUmarul este prim")
else:
    print("Numarul nu este prim")
