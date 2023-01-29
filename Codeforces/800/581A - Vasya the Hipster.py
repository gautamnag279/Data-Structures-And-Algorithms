red, blue = map(int, input().split(" "))
daysWithDiffSocks = min(red, blue)
daysWithSameSocks = (max(red, blue) - min(red, blue))//2
print(daysWithDiffSocks, daysWithSameSocks)
