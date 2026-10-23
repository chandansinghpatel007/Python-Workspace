lower=int(input("Enter the lower range: "))
higher=int(input("Enter the higher range: "))

for i in range(lower,higher+1):
    for j in range(2,i):
        if i%j==0:
            break;
    else:
        print(i)