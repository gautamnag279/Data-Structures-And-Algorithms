def honestWork(task, size):
    boolean = True
    completed = {}
    for i in range(size):
        if task[i] not in completed:
            completed[task[i]] = i
        elif completed[task[i]] < i - 1:
            boolean = False
        else:
            completed[task[i]] = i
    if boolean:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        size = int(input())
        task = input()
        honestWork(task, size)
