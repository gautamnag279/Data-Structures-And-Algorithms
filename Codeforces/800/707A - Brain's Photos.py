# 62 ms, 0 KB
def hashtag(arr):
    colors = ["C", "M", "Y"]
    for i in colors:
        if (i in arr):
            return 1

if __name__ == "__main__":
    rows, columns = map(int, input().split(" "))
    decision = [0]*rows
    for i in range(rows):
        decision[i] = hashtag(list(input().split(" ")))
    if (1 in decision):
        print("#Color")
    else:
        print("#Black&White")
