#Task 8: Sum and average
#Find the sum and average of [10, 20, 30, 40, 50].

numbers = [10, 20, 30, 40, 50]

total = 0
for i in numbers:
    total += i

print(total)
print("Average:", total / len(numbers))