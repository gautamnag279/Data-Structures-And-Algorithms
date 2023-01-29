#Using text warp is much convinient than using the normal method of 'join' and 'for loop'
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string , max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
