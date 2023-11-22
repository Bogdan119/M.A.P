nr_fib=int(input("Pana la ce numar se afiseaza fibbonaci:"))
nr1=0
nr2=1
while nr2+nr1<nr_fib:
    print(nr2+nr1)
    nr1=nr2
    nr2=nr1+nr2
    