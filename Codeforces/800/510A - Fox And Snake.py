rows, colums = map(int, input().split(" "))

for i in range(rows):
    if(i % 2 == 0):
        print("#"*colums)
    elif(i % 4 == 1):
        print("."*(colums-1) + "#")
    else:
        print("#" + "."*(colums-1))
