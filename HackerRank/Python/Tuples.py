if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    x = tuple(integer_list)
    #hash returnes the hash value of the object(which in this case is integer_list)
    print(hash(x))
