from random import randint as r
def tossCube(recursion_deep):
    if recursion_deep <= 0:
        return 0
    return r(1, 6) + tossCube(recursion_deep-1)
print(tossCube(5) / 5)
