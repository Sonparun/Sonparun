from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE


def main():
    sales_file=open('sales.txt','r')
    for line in sales_file:
        amount=float(line)
        print(format(amount,'.2f'))
    sales_file.close()
main()