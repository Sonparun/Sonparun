heroes = ['Ironman', 'Thor', 'Hulk', 'Superman', 'Spiderman']

def Display():
    print(heroes)
    
def add():
    Display()
    Hero = input('Add Heroes : ')
    heroes.append(Hero)
    Display()
def Insert():
    Display()
    Hero = input('Add Heroes : ')
    index = int(input('Insert Heroes :'))
    heroes.insert(index,Hero)
    Display()  
def Remove():
    Display()
    Hero = input('Remove Heroes : ')
    heroes.remove(Hero)
    Display()
    
def DisSort():
    heroes.sort()
    Display()
def Exits():
    name = input('Exits Heroes : ')     
    if(name in heroes ):
        print(name , 'found index = ',len(name))
        Display()
    if(name not in heroes):
        print(name , 'not found')
        Display()    

def main():
    keep = 'y'
    while keep == 'y':
        print('1.Display Heroes Function')
        print('2.Add Heroes Function')
        print('3.Insert Heroes Function')
        print('4.Remove Heroes Function')
        print('5.Display Sorted Heroes Function')
        print('6.Exist Funtion')
        Select = int(input('Please Seclect Funtion : '))
        
        if Select == 1:
            Display()
        elif Select == 2:
            add()
        elif Select == 3:
            Insert()
        elif Select == 4:
            Remove()
        elif Select == 5:
            DisSort()
        elif Select == 6:
            Exits()
        else:
            print('Error Go bruh')
            
        keep = input('Enter y for Moretime: ')
    

main()