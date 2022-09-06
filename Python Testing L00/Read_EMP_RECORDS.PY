
def main():
    emp_file=open('employees.txt','r')
    line1=emp_file.readline()
    while line1 !='':
        line2=emp_file.readline()
        line3=emp_file.readline()
        print('Name: '+line1)
        print('ID:'+line2)
        print('Dept: '+line3)
        line1=emp_file.readline()
    emp_file.close()
main()