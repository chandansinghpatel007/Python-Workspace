#Task 13: Reverse a list
#Reverse a list without using reverse() or slicing [::-1].

numbers = [10, 20, 25, 30, 40]
reversed_numbers = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[i])

print(reversed_numbers)
