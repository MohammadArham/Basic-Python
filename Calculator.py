#Calculator
print("Welcome to calculator, which is developed by Mohammad Arham")
a=int(input("Enter 1st Number:"))
n=input("Enter Operator:")
if n=='+':
    b=int(input("Enter 2nd Number"))
    z=a+b;
elif n=='-':
    b=int(input("Enter 2nd Number"))
    z=a-b;
elif n=='*':
    b=int(input("Enter 2nd Number"))
    z=a*b;
elif n=='/':
    b=int(input("Enter 2nd Number"))
    z=a/b;
elif n=='**':
    b=int(input("Enter 2nd Number"))
    z=a**b;
elif n=='root':
    i=1
    while (i*i<=a):
        z=i;
        i=i+1  
else:
    print("Error! please try again")
if n=='root':
   print("root of",a,"=",z)
else:
    print(a,n,b,"=",z)