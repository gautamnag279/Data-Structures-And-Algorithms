# Enter your code here. Read input from STDIN. Print output to STDOUT
phonebook = {}
entries = int(input())

for n in range(entries):
    name, num = input().strip().split(' ')
    name, num = [str(name), int(num)]
    phonebook[name] = num

while True:
    try:  
        search = str(input())

        if search in phonebook:
            output = ''.join('%s=%r' % (search, phonebook[search]))
            print (output)
        else:
            print ("Not found")
    except EOFError:
        break
