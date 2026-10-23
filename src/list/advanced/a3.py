#Task 20: Move zeros to the end
#Convert [0, 1, 0, 3, 12, 0, 5] to [1, 3, 12, 5, 0, 0, 0], preserving the order of nonzero elements.

numbers = [0, 1, 0, 3, 12, 0, 5]
newList = []

for num in numbers:
    if num != 0:
        newList.append(num)

for num in numbers:
    if num == 0:
        newList.append(num)

print(newList)