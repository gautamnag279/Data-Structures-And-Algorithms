#This code is not acceptable in the solution but is more efficient
s = input()
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)

#Even this code is much better than what hackerRank is accepting
a_string = input().split(' ')
print(' '.join((word.capitalize() for word in a_string)))

#And now here is the code that is acceptable. But this sucks!
def solve(s):
  l1 = s.split(" ")
  s = ""
  for  c in l1:
    s = s + c.capitalize() + " "
    
  return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
