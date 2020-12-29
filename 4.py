# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

s1 = s2 = []
exitFlag = False

for i in range(999**2,100**2,-1):
    for b in range(1000,100,-1):
        if i%b==0 and i/b<1000 :
            s1=list(str(i))
            s2=s1.copy()
            s2.reverse()
            if s2==s1 and exitFlag==False:
                print(i,b)
                exitFlag=True
print('Кінець циклу')
    

    
   
