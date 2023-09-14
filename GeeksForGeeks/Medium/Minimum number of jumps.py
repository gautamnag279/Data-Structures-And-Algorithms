def minJumps(arr, n):
    if arr[0] == 0 and n > 1:
        return -1
    if n == 1:
        return 0

    steps = arr[0]
    max_reach = arr[0]
    jumps = 1

    for i in range(1, n):
        if i == n-1:
            return jumps
        if steps:
            max_reach = max(max_reach, arr[i] + i)
            steps -= 1
        if steps == 0:
            if i >= max_reach:
                return -1
            jumps += 1
            steps = max_reach - i
    return -1
