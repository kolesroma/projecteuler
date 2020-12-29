# Longest Collatz sequence

score = 0
el = 0
elp = 0
element_count = 0
# Подається число ch
for ch in range(1, 1000000):
    element_count = 1
    elp = ch
    #print(ch, score)
    while ch != 1:
        if ch % 2 == 0:
            ch = ch / 2
        else:
            ch = 3*ch + 1
        element_count += 1
    
    if element_count > score:
        score = element_count
        el = elp
    

print(el)
print(score)