s1 = input().lower()
s2 = input().lower()
if(s1 == s2):
    print(0)
else:
    for i in range(len(s1)):
        if(ord(s1[i]) < ord(s2[i])):
            print(-1)
            break
        elif (ord(s1[i]) > ord(s2[i])):
            print(1)
            break

    
