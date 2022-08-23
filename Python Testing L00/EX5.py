number = 0
row=int(input("Enter: "))

for x in range(1,101):
    print(x,end=" ")
    number += 1
    if number % row == 0:
        print("\n")