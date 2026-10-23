#Given this dictionary: student = {'name': 'Chandan', 'age': 20, 'course': 'Python', 'city': 'Hyderabad'}
# Your task:
# 1. Remove the 'city' entry using pop().
# 2. Remove the 'age' entry using del.
# 3. Print the final dictionary.

student = {
    'name': 'Chandan',
    'age': 21,
    'course': 'Python',
    'city': 'Hyderabad'
}

student.pop('city')

del(student['age'])

print(student)