a=int(input('Enter the number : '))
b=int(input('Enter the number : '))
c=int(input('Enter the number : '))

if a==b and b==c:
    print('all value are equqls : ',a,b,c)
elif a>b and a>c:
    print('Grater is a :',a)
elif b>c:
    print('Grater is b :',b)
else:
    print('Grater is c :',c)
    
    