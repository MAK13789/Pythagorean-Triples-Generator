for i in range(1, 100):
    for j in range(1, 100):
        a = i * i
        b = j * j
        c = a + b
        d = c ** 0.5
        e = d.is_integer()
        if (e == True):
            print (i)
            print (j)
            print (d)
            print (" ")
        
