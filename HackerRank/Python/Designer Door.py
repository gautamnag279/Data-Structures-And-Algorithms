#takes the input in integers
N, M = map(int, input().split())

#this prints the first half(from the top) of the figure
for i in range(1,N,2): 
    print((i*'.|.').center(M,'-'))

#this puts the WELCOME part in the bottom
print('WELCOME'.center(M,'-')) 

#this prints the remaining part of the figure
for i in range(N-2,-1,-2): 
    print((i*'.|.').center(M, '-'))
