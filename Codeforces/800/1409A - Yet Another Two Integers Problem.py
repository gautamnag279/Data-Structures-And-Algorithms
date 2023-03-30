def func(a, b):
    diff = abs(a - b)
    moves = diff // 10
    if diff % 10 != 0:
        moves += 1
    print(moves)

if __name__ == "__main__":
    items = int(input())
    for i in range(items):
        a, b = map(int, input().split(" "))
        func(a, b)