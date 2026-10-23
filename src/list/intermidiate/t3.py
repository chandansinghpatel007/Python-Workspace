#Task 12: Search an element
#Check whether 25 exists in [10, 20, 25, 30, 40].

numbers = [10, 20, 25, 30, 40]

found = False

for i in numbers:
    if i == 25:
        found = True
        break

if found:
    print('Element is found')
else:
    print('Element is not found')
    