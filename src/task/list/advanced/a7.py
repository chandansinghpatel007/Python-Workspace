#Task 24: Rotate a list
#Rotate [1, 2, 3, 4, 5] two positions to the right, producing [4, 5, 1, 2, 3].

numbers = [1, 2, 3, 4, 5]

for _ in range(2):
    last = numbers.pop()
    numbers.insert(0, last)

print(numbers)