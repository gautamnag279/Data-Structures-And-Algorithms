# 202 ms, 9200 KB
def getDivision(rating):
    if (rating >= 1900):
        print("Division 1")
    elif (rating >= 1600 and rating <= 1899):
        print("Division 2")
    elif (rating >= 1400 and rating <= 1599):
        print("Division 3")
    else:
        print("Division 4")


if __name__ == "__main__":
    players = int(input())
    for i in range(players):
        getDivision(int(input()))
