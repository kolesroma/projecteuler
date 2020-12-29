# 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


counti=4
exitflag=False
i=1
while True:
    i+=2
    i=str(i)
    ls=list(i)
    i=int(i)
    numsum=0
    tt=0
    for u in range(len(ls)):
        ls[u]=int(ls[u])
        numsum += ls[u]
    if numsum % 3 == 0 or ls[len(ls) - 1] == 0 or ls[len(ls) - 1] == 5 or i % 7 == 0:
        pass
    else:
        #print(i) #Отримуємо непарні числа, які закінчуються не на 0 та не на 5, не діляться на 7
        for p in range(7, i):
            if i % p != 0:
                tt+=1
            if tt == i - 7:
                #print(i) #Виводить всі прості числа                
                counti+=1
                print(counti, i, sep=':')
                if counti==10001:
                    exitflag=True
    if exitflag==True:
        break
        
        
        
        
        
        
    
