def print_formatted(number):
    # biggest binary number
    width = len(str(bin(n)[2:]))
    for i in range(1, n+1):
        #decimal = str(i)
        #octal = str(oct(i)[2:])    
        #hex_ = str(hex(i)[2:]).upper()
        #binary = str(bin(i)[2:])
        x=[str(i) , str(oct(i)[2:]) , str(hex(i)[2:]).upper() , str(bin(i)[2:])]
        #this for loop is to print themin even colums and rows with spaces
        for i in x:
            print(i.rjust(width),end=' ')
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
