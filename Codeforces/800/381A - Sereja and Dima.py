def scoreCard(n, arr):
    scoreSereja = 0
    scoreDima = 0

    for i in range(n):
        if(i%2 == 0):
            cardChosen = max(arr[0], arr[-1])
            scoreSereja += cardChosen
        else:
            cardChosen = max(arr[0], arr[-1])
            scoreDima += cardChosen
        
        if (cardChosen == arr[0]):
            arr.pop(0)
        else:
            arr.pop(-1)

    print(scoreSereja, scoreDima)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    scoreCard(n, arr)
