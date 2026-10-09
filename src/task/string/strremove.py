#Find the given character in String
s=input('Enter the String : ')
ch=input('Enter the character what you remove : ')
str=''
for i in s:
    if i !=ch:
        str+=i;
print('New String : ',str)
