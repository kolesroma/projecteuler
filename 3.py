# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

ch = 2520 
import math
for i in range(1,ch + 1):
    if ch % i == 0:
        ch = ch / i
        print(math.floor(i))
        
print('Остача ділення'+str(ch))

