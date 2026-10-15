#Task 17: Sort without sort()
#Sort [5, 2, 9, 1, 7] in ascending order without using sort() or sorted().

numbers = [5, 2, 9, 1, 7]

for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)
