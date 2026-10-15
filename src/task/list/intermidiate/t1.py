#Task 9: Find the maximum
#Find the largest number in [12, 45, 7, 89, 23] without using max().
#Task 10: Find the minimum
#Find the smallest number without using min().

numbers = [12, 45, 7, 89, 23]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print('Max:', largest, 'Min:', smallest)