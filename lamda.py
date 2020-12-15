def adder(n):

    return lambda a : a * n

myLam = adder(4)
myLam1 = adder(5)

print(myLam(20))
print(myLam1(40))