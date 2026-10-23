#Find the given String is pollydrome are not
s=input('Enter the String : ')
flag=True
for i in range(0,len(s)//2):
    if s[i] !=s[len(s)-1-i]:
        flag=False
        print("Not a pollydrom")

if flag:
    print('Palidrome')
