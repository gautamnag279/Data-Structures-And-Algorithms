s1 = input()
s2 = input()
n = int(input())

def commonLength(s1,s2):
    common = 0
    for i in range(min(len(s1),len(s2))):
        if s1[i] == s2[i]:
            common += 1
        else:
            break
    return common

#the below code 'case' is to check the difference between the sum of len of strings and the common length of the string if it were doubled

case = len(s1) + len(s2) - (2*commonLength(s1,s2))

if case > n:
    print("No")
elif case % 2 == n % 2:
    print("Yes")
elif len(s1) + len(s2) - n < 0:
    print("Yes")
else:
    print("No")
    
