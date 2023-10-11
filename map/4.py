a=int(input("Primul numar:"))
b=int(input("Al doilea numar:"))
i=2

while a!=b:
    
        if a>b:
            a=a-b
        else:
            b=b-a
    
print("Cmmdc al lui",a, ",",b," este:",a)