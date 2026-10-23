#Task 21: Frequency of elements
#Count how often each element appears in [1, 2, 2, 3, 3, 3, 4].

numbers = [1, 2, 2, 3, 3, 3, 4]
counts = []

for num1 in numbers:
    count = 0

    for num2 in numbers:
        if num1 == num2:
            count += 1

    if num1 not in counts:
        counts.append(num1)
        print(f'{num1} appears {count} time(s)')