# 93 ms, 5500 KB
def getTeams(arr):
    programming = []
    math = []
    pe =[]
    for i in range(len(arr)):
        if(arr[i]==1):
            programming.append(i)
        if(arr[i]==2):
            math.append(i)
        if(arr[i]==3):
            pe.append(i)

    ans = min(len(programming), len(math), len(pe))
    print(ans)
    
    for i in range(ans):
        print(math[i] + 1, programming[i] + 1, pe[i] + 1)

if __name__ == "__main__":
    items = int(input())
    getTeams(list(map(int, input().split(" "))))

