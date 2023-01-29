# 124 ms, 6300 KB
def fairPlay(players, strength):
    strength.sort() 
    diff = []
    for i in range(players-1):
        diff.append(strength[i+1] - strength[i])
    print(min(diff))


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        players = int(input())
        playerStrengths = list(map(int, input().split(" ")))
        fairPlay(players, playerStrengths)
