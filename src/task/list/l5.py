#Task 5: Remove elements
#Remove the number 30 from [10, 20, 30, 40, 50]. Also practice pop().

list=[10, 20, 30, 40, 50]
list.remove(30)
print(list)

list.pop(list.index(40))
print(list)