#Task 8: Sum and average
#Find the sum and average of [10, 20, 30, 40, 50].

list=[10, 20, 30, 40, 50]

sum=0
for i in list:
    sum+=i
    
print(sum)

print('Average : ', sum/len(list))