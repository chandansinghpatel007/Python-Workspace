#Task 3: Update an element
#Change the second element of [10, 20, 30, 40] to 100.

list=[10, 20, 30, 40, 50]

for i in range(0,len(list)):
    if i==1:
        list[i]=100
print(list)

