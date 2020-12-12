a = [1, 2, 3, 4]

b = a

print(id(a))
print(id(b))

print(id(a) == id(b))

condition = {''}

if condition:
    print('Evaluated To True')

else:
    print('Evaluated To False')