def isEven(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"
print(isEven(int(input("Set the number: "))))