#Task 19: Merge two lists
#Merge two lists and create a third list containing all elements in sorted order.

list1 = [5, 2, 8]
list2 = [3, 1, 7]
numbers = []

for num in list1:
    numbers.append(num)

for num in list2:
    numbers.append(num)

for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)  
