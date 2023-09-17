def printFibb(n):
    if n == 1:
        return [1]

    sequence = [1, 1]

    while len(sequence) < n:
        next = sequence[-1] + sequence[-2]
        sequence.append(next)

    return sequence
