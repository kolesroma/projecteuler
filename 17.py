# Number letter counts

letter_count = 0

word = input()
ls = [c for c in word if c != ' ']

for i in range(ls.count('-')):
    ls.remove('-')
    
letter_count += len(ls)

print(ls)
print(letter_count)



