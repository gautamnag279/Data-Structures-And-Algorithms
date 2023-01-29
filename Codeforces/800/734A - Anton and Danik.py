n = int(input())
games = list(input().lower())

if(games.count('a') > games.count('d')):
    print("Anton")
elif(games.count('a') < games.count('d')):
    print("Danik")
else:
    print("Friendship")
