import math
a=float(input("Primul nr"))
b=float(input("Al doilea nr"))
c=float(input("Al 3 nr"))

delta=float
x1=float
x2=float

delta=(b**2)-(4*a*c)
if delta>0:
    delta=math.sqrt(delta)
    x1=(-b+delta)/2*a
    x2=(-b-delta)/2*a

    print("X1 este:",x1)
    print("X2 este:",x2)
else:
    print("unsolvable")

