def minion_game(string):
    string = string.upper()
    countKevin = 0
    countStuart = 0
    
    for i in range(len(string)):
    #Note that it is "len(string) - i" and not "len(string) - 1"
        if string[i] in ['A' , 'E' , 'I' , 'O' , 'U']:
            countKevin = countKevin + (len(string) - i)
        else:
            countStuart = countStuart + (len(string) - i)
    
    if countKevin > countStuart:
        return print("Kevin " + str(countKevin))
    elif countStuart > countKevin:
        return print("Stuart " + str(countStuart))
    elif countKevin == countStuart:
        return print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
