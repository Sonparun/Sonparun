x=int(input("w"))
y=0
z=100//x + (0 if 100 % x == 0 else 1)
for i in range(1,101):
    y+=1
    if z==y:
        print(i,end='\n')
        y=0
        continue
    print(i,end='\t')