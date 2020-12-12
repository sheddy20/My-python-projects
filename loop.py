numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Break keyword
for n in numbers:
    if n == 9:
        print('found it ')
        break
    print(n)


# Continue Keyword
for j in numbers:
    if j == 3:
        print('skip number three')
        continue 
    print(j)