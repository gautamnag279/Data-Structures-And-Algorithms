levels = int(input())
x = [int(i) for i in input().split(" ")][1:]
y = [int(i) for i in input().split(" ")][1:]
arr = len(set(x+y))

if(arr == levels):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
