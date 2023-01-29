def findNumbers(lst):
    lst.sort()
    for i in range(0, 3):
        print((lst[3] - lst[i]), end = " ")

lst = list(map(int, input().split(" ")))
findNumbers(lst)
