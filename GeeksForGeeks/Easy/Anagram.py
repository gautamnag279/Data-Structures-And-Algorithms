def isAnagram(self,a,b):
    if len(a) > len(b):
        for i in set(a):
            if i not in b or a.count(i) != b.count(i):
                return False
    else:
        for i in set(b):
            if i not in b or b.count(i) != a.count(i):
                return False
    return True