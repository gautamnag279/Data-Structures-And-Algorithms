num = int(input(""))

if num%2 != 0:
    print("Weird")
    
if num %2 == 0:
    if 2 <= num <= 5:
        print("Not Weird")
    if 6 <= num <= 20:
        print("Weird")
    if num > 20:
        print("Not Weird")
