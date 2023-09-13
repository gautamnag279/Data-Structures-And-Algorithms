def duplicates(arr, n):
    seen, duplicates = set(), set()

    for i in arr:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)

    if not duplicates:
        return [-1]
    return sorted(list(duplicates))
