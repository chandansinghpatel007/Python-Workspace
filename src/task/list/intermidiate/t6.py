#Task 15: Second-largest number
#Find the second-largest distinct number in [10, 40, 20, 40, 30].

numbers = [10, 40, 20, 40, 30]

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num < largest:
        second_largest = num

if second_largest == float('-inf'):
    print("No second-largest distinct number")
else:
    print("Second largest:", second_largest)

