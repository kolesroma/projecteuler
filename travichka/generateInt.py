from random import randint as r
def generateInt(recursion_deep):
    if not recursion_deep:
        return 0
    return r(3, 7)**2 + generateInt(recursion_deep-1)
print(generateInt(3))
