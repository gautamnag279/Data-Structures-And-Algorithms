import xml.etree.ElementTree as etree

maxdepth = -1
def depth(elem, level):
#your code goes here
    global maxdepth
    if level == maxdepth:
        maxdepth += 1
    for i in elem:
        #using recursion. For help go here - https://stackoverflow.com/questions/479343/how-can-i-build-a-recursive-function-in-python
        depth(i , level + 1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
