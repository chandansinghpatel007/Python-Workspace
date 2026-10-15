#Task 15: Second-largest number
#Find the second-largest distinct number in [10, 40, 20, 40, 30].

numbers = [10, 40, 20, 40, 30]
unique = sorted(set(numbers))

if len(unique) < 2:
    print("No second-largest distinct number")
else:
    print(unique[-2])

