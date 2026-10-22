#Task 18: Find common elements
#Find common elements between [1, 2, 3, 4, 5] and [3, 4, 5, 6, 7].

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [3, 4, 5, 6, 7]
common = []

for num in numbers1:
    if num in numbers2 and num not in common:
        common.append(num)

print(common)