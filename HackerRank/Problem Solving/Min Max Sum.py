arr = list(map(int, input().rstrip().split()))
print(sum(arr) - max(arr), sum(arr) - min(arr))
