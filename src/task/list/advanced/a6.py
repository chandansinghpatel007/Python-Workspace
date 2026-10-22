#Task 23: Flatten a nested list
#Convert [[1, 2], [3, 4], [5, 6]] into [1, 2, 3, 4, 5, 6].

nested_list = [[1, 2], [3, 4], [5, 6]]

flattened_list = [
    number
    for sublist in nested_list
    for number in sublist
]

print(flattened_list)