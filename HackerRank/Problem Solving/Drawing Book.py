book_length = int(input())
page = int(input())

turns = min(page/2 , book_length/2 - page/2)
print(int(turns))
