def sum_of_round(n):
    lst = [int(i) for i in (str(n)[::-1])]
    ans = [0] * len(lst)
    for i in range(len(lst)):
        ans[i] = lst[i] * (10**i)
 
    res = [i for i in ans if i != 0]
    print(len(res))
    print(*(res[::-1]))
 
n = int(input())
for i in range(n):
    sum_of_round(int(input()))
