a=800
b=800
c=800
while a<0 or a>360:
    a=int(input("Primul unghi sa fie mai mic de 360 si mai mare de 0:"))
while b<0 or b>360:
    b=int(input("Al doilea unghi sa fie mai mic de 360 si mai mare de 0:"))
while c<0 or c>360:
    c=int(input("Al treilea unghi sa fie mai mic de 360 si mai mare de 0:"))

if a+b+c!=180:
    print("Nu sunt bune unghiurile")
else:
    print("Sunt bune unghiurile")

