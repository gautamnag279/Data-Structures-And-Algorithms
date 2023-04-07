def squareArea(length, breadth):
    longestSide = max(length, breadth)
    shortestSide = min(length, breadth)
    if (shortestSide*2) < longestSide:
        minArea = (longestSide)**2
    else:
        minArea = (shortestSide*2)**2
    print(minArea)

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        length, breadth = map(int, input().split())
        squareArea(length, breadth)