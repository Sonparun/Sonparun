# records={'6506022620095':['Anirach Mingkwan','Anirach@gmail.com','0817320766']}


# print('1.Display Record')
# print('2.Serach [ID]')
# print('3.Add')
# print('4.Modify Records[ID]')
# print('5.Delete [ID}')
# print('6.Exit')

# opt=int(input('Enter number for operation: '))

# if opt == 1 :
#     print(records)
# elif opt ==2 :
#     key=int(input('Serach ID: '))
#     for key in records:
#         print(key,'Your ID record is: ',records[key])
# elif opt == 3:
#     idadd=int(input('Add new ID: '))
#     nameadd=str(input('Add new name: '))
#     emailadd=input('Add new email: ')
#     phoneadd=int(input('Add phone numer: '))
# else:
#     print('Ending operation')


# 1 แสดงข้อมูล display reccord 
# 2search ID 
# 3Add 
# 4modifide reccord แก้ไข 
# 5del reccord 
# 6exist record
records={'6506022620095':['Anirach Mingkwan','Anirach@gmail.com','0817320766']}

print(records)

#1Display
def Display():
    print(records)
def Search():
    search = input('Please Search : ')
    print(records.keys(),records.get(search))
def Add():
    Display()
    addKey = input('Add Enter ID: ')
    addName = input('Add Enter Name: ')
    addMail = input('Add Enter Email: ')
    addPhone = input('Add Enter Phone Number: ')
    records[addKey] = addName , addMail , addPhone
    print(records)
def Modifier():
    Display()
    addKey = input('Modifier Enter ID: ')
    addName = input('Modifier Enter Name: ')
    addMail = input('Modifier Enter Email: ')
    addPhone = input('Modifier Enter Phone Number: ')
    records[addKey] = addName , addMail , addPhone
    print(records)
def Del():
    addKey = input('Delete Enter ID: ')
    records.pop(addKey)
    print(records)
def Exits():
    name = input('Exits ID : ')     
    if(name in records ):
        print(name , 'found index = ',len(name))
        Display()
    if(name not in records):
        print(name , 'not found')
        Display()    

def main():
    keep = 'y'
    while keep == 'y':
        print('1.Display')
        print('2.Search [ID]')
        print('3.Add')
        print('4.Modifier [ID]')
        print('5.Delete [ID]')
        print('6.Exist')
        Select = int(input('Seclect Operation : '))
        
        if Select == 1:
            Display()
        elif Select == 2:
            Search()
        elif Select == 3:
            Add()
        elif Select == 4:
            Modifier()
        elif Select == 5:
            Del()
        elif Select == 6:
            Exits()
        else:
            print('Error')
            
        keep = input('Enter y for Moretime Enter n for Exit: ')
main()