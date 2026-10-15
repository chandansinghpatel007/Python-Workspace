#Task 14: Remove duplicates
#Convert [1, 2, 2, 3, 4, 4, 5] into a list containing unique elements, preserving order.

numbers = [1, 2, 2, 3, 4, 4, 5]
result = []

for num in numbers:
    if num not in result:
        result.append(num)

print(result)
