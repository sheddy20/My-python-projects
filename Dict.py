student = {

    'name': 'Maxwell',
    'age': 20,
    'courses': [
        'Math',
        'Chemistry',
        'Physics',
        'Geography',
        'CompSci'
    ],
}

# Get Method
student['Country'] = 'Armenia'

iterable = len(student)
print(iterable)

keys = student.keys()
print(keys)

for students in student.items():
    print(student)

# Update Method
student.update({'name': 'Mantock', 'age': 35, 'Country': 'Kosovo', 'continent': 'Europe', 'isNew': True})

# Delete Method
del student['age']
del student['isNew']

for key, value in student.items():
    print(f'Keys are: {key}, values are: {value}')

popUp = student.pop('Country')
print(popUp)

print(student)