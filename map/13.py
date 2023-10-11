s=0
m=0
contor=1
nr=int(input("Dati numarul de numere:"))

while contor<=nr:
    a=int(input("Nr:"))
    s=s+a
    contor+=1

print("Suma:",s)
print("Media:",s/nr)