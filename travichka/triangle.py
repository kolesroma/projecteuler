coord1 = list(map(int, input("1: input 2 numbers separate with space: ").split()))
coord2 = list(map(int, input("2: input 2 numbers separate with space: ").split()))
coord3 = list(map(int, input("3: input 2 numbers separate with space: ").split()))

# determines the length of triangle`s side between two points
def length(ls2, ls1):
    return sum([(ls2[i]-ls1[i])**2 for i in range(2)]) ** 0.5

a = length(coord1, coord2)
b = length(coord2, coord3)
c = length(coord3, coord1)

# returns the square of triangle using Heron`s formula
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p-a) * (p-b) * (p-c)) ** 0.5

print(heron(a, b, c))