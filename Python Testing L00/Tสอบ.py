# name=str(input("Enter your name = "))

# print("'Types of Photo")
# print('1.One icnh')
# print('2.Two icnh')
# print('3.Polaroid')

# typesphoto=int(input('Select type = '))
# discount=0

# if typesphoto == 1 :
#     amount=int(input('Enter amount = '))
#     price=65
#     all=price*amount
#     if amount >= 3 :
#         discount=((all/100)*5)
#         sum=all-discount

# elif typesphoto == 2 :
#     amount=int(input('Enter amount = '))
#     price=80
#     all=price*amount
#     if amount >= 3 :
#         discount=((all/100)*5)
#         sum=all-discount

# elif typesphoto == 3 :
#     amount=int(input('Enter amount = '))
#     price=70
#     all=price*amount
# else :
#     ('Error Orders')


# print('Show Details')
# print('Your name is ',name)

# if typesphoto == 1 :
#     print('Type of photo is One icnh')
# elif typesphoto == 2 :
#     print('Type of photo is Two icnh')
# elif typesphoto == 3 :
#     print('Type of photo is Polaroid')
# else :
#     print('Error Orders')

# print('Amount is ',amount)
# print('Total price is',price,'*',amount,' = ',all)
# print('Discount = ',discount)
# print('Net price = ',sum)


name=str(input("Enter your name = "))

print("'Types of Photo")
print('1.One icnh')
print('2.Two icnh')
print('3.Polaroid')

typesphoto=int(input('Select type = '))
discount=0

if typesphoto == 1 :
    amount=int(input('Enter amount = '))
    price=65
    all=price*amount
    if amount >= 3 :
        discount=((all/100)*5)
        sum=all-discount

elif typesphoto == 2 :
    amount=int(input('Enter amount = '))
    price=80
    all=price*amount
    if amount >= 3 :
        discount=((all/100)*5)
        sum=all-discount

elif typesphoto == 3 :
    amount=int(input('Enter amount = '))
    price=70
    all=price*amount
    sum=all


print('Show Details')

if typesphoto == 1 :
    print('Your name is ',name)
    print('Type of photo is One icnh')
    print('Amount is ',amount)
    print('Total price is',price,'*',amount,' = ',all)
    print('Discount = ',discount)
    print('Net price = ',sum)
elif typesphoto == 2 :
    print('Your name is ',name)
    print('Type of photo is Two icnh')
    print('Amount is ',amount)
    print('Total price is',price,'*',amount,' = ',all)
    print('Discount = ',discount)
    print('Net price = ',sum)
elif typesphoto == 3 :
    print('Your name is ',name)
    print('Type of photo is Polaroid')
    print('Amount is ',amount)
    print('Total price is',price,'*',amount,' = ',all)
    print('Discount = ',discount)
    print('Net price = ',sum)
else :
    print('Error Orders')
