cars = ['Toyota', 'mercedes', 'BMW', 'Bugatti', 'Volkswagen', 'cadilac']

for index, car in enumerate(cars, start=1):

    print(index, car)


newList = ' - '.join(cars)

oldList = newList.split(' - ')

name = 'shedrack'

value = '-'.join(name)
newValue = value.split(' - ')

print(newValue)
print(value)

print(oldList)
print(newList)