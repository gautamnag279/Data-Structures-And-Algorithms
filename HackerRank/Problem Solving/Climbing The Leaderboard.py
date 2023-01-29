elements = int(input())
ranked = map(int , input().split())

player = int(input())
player_score = map(int , input().split())

leaderboard = sorted(set(ranked) , reverse = True)
last_position = len(leaderboard)

for i in player_score:
    while (last_position > 0) and (i >= leaderboard[last_position - 1]):
        last_position = last_position - 1
    print(last_position + 1)
    
