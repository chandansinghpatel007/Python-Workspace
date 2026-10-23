#Find the given character in String
s=input('Enter the String : ')
ch=input('Enter the character what you search : ')
c=0
for i in s:
    if i ==ch:
        c+=1;
print('String character count : ',c)
