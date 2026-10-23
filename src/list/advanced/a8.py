#Task 25: Student marks analyzer
#Given marks = [78, 45, 90, 32, 67, 90, 56], find the average, highest mark, lowest mark, 
# number of passes (marks >= 40), and second-highest distinct mark.

marks = [78, 45, 90, 32, 67, 90, 56]

average = sum(marks) / len(marks)
highest_mark = max(marks)
lowest_mark = min(marks)
pass_count = sum(1 for mark in marks if mark >= 40)
second_highest = sorted(set(marks))[-2]

print(f"Average: {average:.2f}")
print(f"Highest mark: {highest_mark}")
print(f"Lowest mark: {lowest_mark}")
print(f"Number of passes: {pass_count}")
print(f"Second-highest distinct mark: {second_highest}")