⁸while True:
    import time as t
    vybor = int(input('write one of the following numbers corresponding to the programs \n 1 - acquaintance\n 2 - LCD and LCM of two numbers\n 3 - \n 4 - sum of cubes and sum of factorials \n 5 - missing number\n 6 - n-th Fibonacci number \n 7 - greatest number of consecutive numbers equal to each other\n 8 - the greatest integer power of two not exceeding\n 9 - poor snail\n 10 - clock hand\n'))
    def fac(n):
        for i in range(1, n + 1):#factorial formula
            n *= i
        return n
    
    
    # 1 excercise    
    
    
    if vybor == 1
        p1 = 0             #setting variables
        st = "an entrepreneur"
        n1 = input("what's your name? \n")
        a1 = int(input("how old are you? \n"))
        for i in range(7, 100):           #define the gap
            if a1 == i and a1 <= 17:        #put if for first case and change the meaning of variables
                s = a1 - 6
                st = f"in {s} class"
            elif a1 == i and a1 <= 21:      #elif for other case and change the meaning again
                s1 = a1 - 17
                st = f"at {s} course"
        for i in range(15, 100):      #gap for users, who has programming experience
            if i == a1:
                p1 = a1 - 14
        print(f"hello, {n1}! you're {st} and have {p1} year(s) of programming experience. sounds cool!")  #outpul result         
        t.sleep(7)# the enddd


    # 2 excercise


    if vybor == 2:
        print('Enter two integers: ', end='')
    n, k = map(int, input().split())
    a, b = n, k
    while 1:                #euclid 's algorithm for нод(a,b)
        if(a == 0 or b == 0): break;
        if a > b:
            a = a % b
        else:
            b = b % a
        print('least common divisor(', n, ', ' , k, ')', ' = ', a + b, sep='')
        print('least common multiple(', n, ', ', k, ')', ' = ', int(n * k / (a + b)), sep='') #using the property нод(a,b)*нок(a,b)=a*b



    # 3 excercise


    if vybor == 3:
        n3, k3 = map(int, input('type two whole numbersseparated by space (the first has to be higher than second):\n ').split())
        srarfm3 = 0
        srgarm3 = 0
        max31 = -9999999999999
        max32 = -98888888
        min31 = 9999999999
        min32 = 988888888
        for j in range(k3):
            chsl3 = int(input())
            srarfm3 += chsl3
            srgarm3 +=  (1 / chsl3)
            if chsl3 > max31:
                max32 = max31 
                max31 = chsl3
            if chsl3 > max32 and chsl3 != max31:
                max32 = chsl3
            if chsl3 < min31:
                min32 = min31
                min31 = chsl3
            if chsl3 < min32 and chsl3 != min31:
                min32 = chsl3
        for i in range(n3 - k3):
            zachemmm = int(input())
        print('a. Average -',srarfm3 / k3, '\nb. Harmonic mean -', srgarm3 / k3, '\nc. Maximum element -', max31, '\nd. Second maximum element -',max32,'\ne. Minimum element -',min31,'\nf. Second minimum element -', min32)

    # 4 excercise


    if vybor == 4:
        sumcub = 0    # iznachalno numbers == 0 and then we'll adding positions
        sumfac = 0
        n4 = int(input('enter an integer \n'))
        for i in range(n4 + 1):
            sumcub += i ** 3    # adding cubes of all nums
            sumfac +=  fac(i)   # using functions of factorial and adding every to every
        print('sum of cubes -',sumcub,'sum of factorials -', sumfac)    #output znachenya
        t.sleep(7)    # give to user time to understand the answer


    # 5 excercise


    if vybor == 5:    #start
         m0 = []      #enter variables 
         m = []
         b = 0        
         j = 0
         k = 1
         n = int(input('type a natural number ')) #user introduces his own numbers
         for i in range(1, n+1):      #range to denote the gap
             b += 1
             m0.append(b)
         print(f'type in {n-1} numbers between 1 and {n} included')       #ask user to put more numbers
         for i in range(1, n):         #gap
             a = int(input())           #numbers, which were introduced 
             m.append(a)                #append to add a
         while m[j] == m0[j]:          #appeal (?) to d
             k += 1          #increase variables
             j += 1
         print(k)    #giving out missing number
         t.sleep(7)   


    # 6 excercise


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


    # 7 excercise


    if vybor == 7:
        


    # 8 excercise

    
    if vybor == 8:
        n8 = int(input('please, enter natural number \n'))    # take number
        largchisl = 0   # zero peremennaya
        for k in range(n8):    # check every number less, then unputed
            if k & (k - 1) == 0:     # if this number bitwise "AND" with this num -1 equals zero its one hundred percent stepen of two
                x = k                # adding into a pure variable every power of two replacing the previous one less than a given number
        print('the largest power of two not exceeding this number -', largchisl)    #output answer
        t.sleep(7)


    # 9 excercise

    if vybor == 9:
        day = 0
        h, a, b = map(int, input('Enter positive numbers:\npit height value <h>, value <a> and value <b> (where a is up, b is down):\n'). split(';'))
        if a < b or (a == b and h > a):
            print('Will never get out of the pit')
        if a == b and h < a:
            print('Number of day: 1')
        else:
            while 1:
                day += 1
                h = h - a
                if h <= 0: break
                h = h + b
        print('Number of day:', day)
    # 10 excercise


    if vybor == 10:
        a10 = float(input('Enter how many degrees the hour hand has turned since the beginning of the day '))    # input number of degreees
        hours = int(a10 // 30)   # finding number of hours
        minuts = int(a10 % 30 // 0.5)   # it`s finding of minutes
        seconds = int(((a10 % 30) % 0.5) // (1/120))   # and it`s seconds
        print('hours,', hours, ' minuts,' minuts,', seconds, 'seconds')    # output answer
        t.sleep(7)
