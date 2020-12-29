# Power digit sum

a = 2**1000
count = 0
ls = [int(c) for c in str(a)]
for i in ls:
    count += i
print(count)