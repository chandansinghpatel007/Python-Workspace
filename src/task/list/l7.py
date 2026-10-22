#Task 7: List length
#Find how many elements are present in a list without manually counting them.

numbers = [10, 20, 30, 40, 50]

print(len(numbers))

count = 0
for i in numbers:
    count = count + 1

print(count)
