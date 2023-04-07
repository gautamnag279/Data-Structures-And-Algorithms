def probability(yakko, wakko):
    a = 0
    reference = {1: "1/6", 2: "1/3", 3: "1/2", 4: "2/3", 5: "5/6", 6: "1/1"}
    highest = max(yakko, wakko)
    for i in range(highest, 7):
        if i >= highest:
            a += 1
    print(reference[a])


if __name__ == "__main__":
    yakko, wakko = map(int, input().split())
    probability(yakko, wakko)
