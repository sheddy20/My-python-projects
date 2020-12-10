courses = ['History', 'chemistry', 'compSci', 'Geography', 'math']

# Slice method in python
print(courses[0:4])


# Append Method
courses.append('Economics')

higherCourses = ['DeepLearning', 'Machine Learning', 'Neural Network', 'CNN', 'RNN']

courses.extend(higherCourses)

courses.remove('CNN')

courses.append('Scikit Learn')


courses.insert(0, 'Reinforcement Learning')

courses.pop()

deletedCourse = courses.pop()

print(deletedCourse)

courses.sort()
print(courses)





