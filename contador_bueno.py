def primos():
    primo= [2]
    nmax = 1000
    for x in range(3, nmax):
        for i in range(2, x):
            if x%i != 0:
            
                continue
            else:
            
                break 
        else:
        
            print "%d es primo" %x
            primos.append(x)
        F = open('numerosprimos.txt', 'w')
    for data in primos:
        F.write('%d\n'%data)
