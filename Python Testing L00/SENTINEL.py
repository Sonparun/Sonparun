
check='y'
while check=='y':
    item=float(input("Enter the iten wholesale cost: "))
    retail_price=item*2.5
    print("Retail price $", format (retail_price,",.2f"),sep='')
    check=input("Do you have another item?(Enter y for yes): ")