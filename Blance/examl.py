
# numberSplit(4)  --> [2, 2]
# numberSplit(10) --> [5, 5]
# numberSplit(11) --> [5, 6]
# numberSplit(-5) --> [-5, -4]


# numberSplit1 = 4
# numberSplit2 = 10
# numberSplit3 = 11
# numberSplit4 = -9

# numberSplit11=numberSplit1.split()

# print(numberSplit11)


from math import floor


def numberSplit(num):
    num1=floor(num/2)
    num2=num-num1
    return [num1,num2]
print(numberSplit(4))
print(numberSplit(10))
print(numberSplit(11))
print(numberSplit(-9))