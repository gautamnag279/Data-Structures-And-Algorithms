from math import ceil, floor

def denomination(amount):
    c1 = floor(amount/3)
    c2 = ceil(amount/3)

    if (c1 + 2*c2 == amount):
        print(c1, c2)
    else:
        print(c2, c1)

if __name__ == "__main__":
    testCases = int(input())
    for i in range(testCases):
        denomination(int(input()))