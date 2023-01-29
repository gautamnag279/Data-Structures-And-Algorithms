import textwrap

def merge_the_tools(string, k):
    words = textwrap.fill(string,k).split()
    for i in words:
        letters = i[0]
        for j in i:
            if j not in letters:
                letters = letters + j
        print(letters)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
    
#This is another way of doing it
def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        print("".join(dict.fromkeys(string[i:i+k])))
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
