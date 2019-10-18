# con este progama va a determinar que numeros sin primos y cuales no#
def primos_ya():
    print "este programa se va encargar de decirte cuales son primos y cuales no"
    n=input("hasta que numero cuento?")
    primo=True
    for i in range(1,n+1):
        for p in range(2,i-1):
            if (i%p==0):
                primo=False
        if (primo==False):
                print "i=",i, "no primo"
        else:
                print "i=",i, "es primo"
        primo=True

primos_ya()
               
