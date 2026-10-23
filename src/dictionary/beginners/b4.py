#Given this dictionary: student = {'name': 'Chandan', 'age': 20, 'course': 'Python', 'city': 'Hyderabad', 'grade': 'A'}
#Your task:
#1. Change 'age' from 20 to 21.
#2. Change 'course' from 'Java' to 'Python'.
#3. Print the updated dictionary.

student = {
    'name': 'Chandan',
    'age': 20,
    'course': 'Java',
    'city': 'Hyderabad'
}

student['age'] = 21
student['course'] = 'Python'

print(student)