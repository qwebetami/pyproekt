while True:
    import time as t
    vybor = int(input('write one of the following numbers corresponding to the programs \n 1 - \n 2 - \n 3 - \n 4 - sum of cubes and sum of factorials \n 5 - \n 6 - n-th Fibonacci number \n 7 - \n 8 - \n 9 - \n 10 - \n'))
    def fac(n):
        for i in range(1, n + 1):#factorial formula
            n *= i
        return n

    
    # 4 excercise

    if vybor == 4:
        sumcub = 0    # iznachalno numbers == 0 and then we'll adding positions
        sumfac = 0
        n4 = int(input('enter an integer \n'))
        for i in range(n4 + 1):
            sumcub += i ** 3    # adding cubes of all nums
            sumfac +=  fac(i)   # using functions of factorial and adding every to every
        print('sum of cubes -',sumcub,'sum of factorials -', sumfac)    #output znachenya
        t.sleep(7)
    
    #6 excercise

    if vybor == 6:
        f0 = 0    # given zero 
        f1 = 1    # given one 
        n6 =  int(input('enter a natural number \n'))    #input num for n-th Fibonacci number
        if n6 == 0:
            print(1)
        elif n6 > 0:
            for i in range(2, n6+1):
                f0, f1 = f1, f0 + f1
            print(f1)
        t.sleep(7)

    
    # 8 excercise

    
    if vybor == 8:
        n8 = int(input('please, enter natural number \n'))
        largchisl = 0   
        for k in range(n8):    
            if k & (k - 1) == 0:    
                x = k                       
        print('the largest power of two not exceeding this number -', largchisl)
        t.sleep(7)