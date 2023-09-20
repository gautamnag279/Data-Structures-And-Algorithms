def rotate(N, D):
    binary = bin(N)[2:]
    binary = '0' * (16 - len(binary)) + binary
    D = D % 16

    rotatedLeft = binary[D:] + binary[:D]
    rotatedRight = binary[-D:] + binary[:-D]

    return int(rotatedLeft, 2), int(rotatedRight, 2)