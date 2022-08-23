
row=int(input('How many rows? '))
column=int(input('How many columns? '))

for row in range(1,row+1):
    print('*', end = "")
    for column in range(1,column+1):
        print('*', end = "")
    print()