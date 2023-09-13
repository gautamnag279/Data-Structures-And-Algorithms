def ispar(x):
    limit = float('inf')
    while (len(x) < limit):
        limit = len(x)
        x = x.replace("()", "")
        x = x.replace("{}", "")
        x = x.replace("[]", "")
    if len(x):
        return False
    return True


s = "(){(}[])}"
print(ispar(s))
