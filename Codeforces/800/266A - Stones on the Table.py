num = int(input())
string = input()
count = 0
for i in range(0, num - 1):
    if string[i] == string[i+1]:
        count += 1
print(count)
