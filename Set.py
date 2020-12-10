sc_courses = {'Physics', 'Chem', 'Geo', 'Math', 'Eng', 'Bio'}
art_courses = {'Gov', 'Econs', 'Lit', 'Math', 'Eng', 'Music'}

# Difference Method
diff = sc_courses.difference(art_courses)
diff2 = art_courses.difference(sc_courses)

# Intersection Method
Inter = sc_courses.intersection(art_courses)
print(Inter)

# Union Method
union = art_courses.union(sc_courses)
print(union)


print(diff)
print(diff2)