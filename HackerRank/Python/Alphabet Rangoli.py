def print_rangoli(size):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    array = []
    for i in range(size):
        line = alphabet[i:size]
        line = line[:0:-1] + line
        array.append('-'.join(line.center(size*2-1, '-')))
				
    for row in array[:0:-1]:
        print(row)
    for row in array:
        print(row)
