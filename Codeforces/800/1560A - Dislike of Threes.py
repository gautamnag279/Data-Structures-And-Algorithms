# 62 ms, 1600 KB
def scoreCard(x):
    arr = [i for i in range(1667) if i%3 != 0 and i%10 != 3]
    print(arr[x - 1])

# main function
if __name__ == "__main__":
    items = int(input())
    for i in range(items):
        scoreCard(int(input()))
