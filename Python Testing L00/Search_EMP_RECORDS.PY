def main():
    emp_file=open('employees.txt','r')
    line=input('Enter name: ')
    while line != '':
        name=emp_file.readline()
        id=emp_file.readline()
        dept=emp_file.readline()
        print(name)
        line=emp_file.readline()
main()