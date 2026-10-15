#Task 11: Count even and odd numbers
#Count how many even and odd numbers are in [1, 2, 3, 4, 5, 6, 7, 8].


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

ecount = 0
ocount = 0

for i in numbers:
    if i %2==0 :
        ecount=ecount+1
    else :
        ocount = ocount+1

print('Even Count:', ecount, 'Odd Count:', ocount)