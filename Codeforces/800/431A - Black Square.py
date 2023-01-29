# 61 ms, 2600 KB
def energyUsed(m, p):
    total = 0
    for i in positions:
        total += maping[i - 1]
    print(total)

if __name__ == "__main__":
    maping = list(map(int, input().split(" ")))
    positions = [int(i) for i in input()]
    energyUsed(maping, positions)
