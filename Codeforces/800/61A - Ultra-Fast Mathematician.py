str1 = input()
str2 = input()
ans = ""
for i in range(len(str1)):
    if str1[i] != str2[i]:
        ans += '1'
    else:
        ans += '0'
print(ans)
