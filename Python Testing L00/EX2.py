wh=float(input('Enter the number of hours worked: '))
pr=float(input('Enter the hourly pay rate: '))
ot=wh-40

if wh > 40:
    s=(40*pr)+(ot*(1.5*pr))

else :
    s=wh*pr
print('The gross pay is ${:,.2f}' .format(s))