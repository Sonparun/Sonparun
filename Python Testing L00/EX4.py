print("Please select operation -")
print("1.Add")
print("2.Subtract")
print("3.Mutiply")
print("4.Divide")


x=int(input("Selecet operations from 1,2,3,4 : "))

if x==1:
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    c=a+b
    print(a,"+",b,"=",c)
elif x==2:
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    c=a-b
    print(a,"-",b,"=",c)
elif x==3:
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    c=a*b
    print(a,"*",b,"=",c)
elif x==4:
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    c=a/b
    print(a,"/",b,"=",c)
else:
    print("Operations error")