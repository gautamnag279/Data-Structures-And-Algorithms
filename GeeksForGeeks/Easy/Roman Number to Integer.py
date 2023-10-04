n = "XV"
length = len(n)

reference = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

total = 0
i = 0

while i < length - 1:
    if reference[n[i]] < reference[n[i+1]]:
        total -= reference[n[i]]
    else:
        total += reference[n[i]]
    i += 1

total += reference[n[i]]

print(total)
