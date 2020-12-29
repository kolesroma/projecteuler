# Summation of primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

counti=4
exitflag=False
i=1
totalsum=2+3+5+7

while True:
    i+=2
    numsum=0
    tt=0
    if i % 10 == 1 or i % 10 == 3 or i % 10 == 7 or i % 10 == 9:
        if i % 3 != 0:
            #print('maybe proste')
            for p in range(7, i):
                if i % p != 0:
                    tt+=1
                if tt == i - 7:               
                    counti+=1
                    if i<2000000: #Сума простих чисел до [число]
                        totalsum+=i
                    else:
                        exitflag=True
                    #print(counti, i, sep=':')               
                        
    if exitflag==True:
        break
print('totalsum = ',totalsum)
        
        
        
        
        
        
    
