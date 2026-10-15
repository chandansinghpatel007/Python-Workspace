#Task 16: Separate positive and negative
#From [-5, 10, -2, 8, 0, -7], create separate lists for positive, negative, and zero values.

numbers = [-5, 10, -2, 8, 0, -7]
positive = []
negative = []
zero = []

for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero.append(num)

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
