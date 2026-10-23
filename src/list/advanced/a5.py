#Task 22: List comprehension
#Create a list of squares of all even numbers from 1 to 20 using list comprehension.

squares = [
    number ** 2 
    for number in range(1, 21) 
    if number % 2 == 0
]

print(squares)