id_code=input('Enter code item = ')
price=float(input('Enter price item = '))
amount=float(input('Enter amount item = '))
discount=0
if id_code[1] == '1' :
    sum=price*amount
    discount=sum * 0.03
    total=sum-discount
    print('Discount = ',discount)
    print('Total price = ',total)

elif id_code[1] == '2' :
    sum=price*amount
    discount=sum * 0.03
    total=sum-discount
    if amount > 3 :
        discount=sum * 0.05
        total=sum-discount
    print('Discount = ',discount)
    print('Total price = ',total)
else :
    sum=price*amount
    total=sum-discount
    print('Discount = ',discount)
    print('Total price = ',total)