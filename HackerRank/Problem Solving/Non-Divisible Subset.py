n , k = [int(i) for i in input().strip().split()]
#The array 's' stores the remainder when divided by k. this is done because if the sum of two numbers (say A and B) if divieible by a number k, then the sum of remainders of those numbers
#when divided by K, will give K (i.e. A%K + B%K == K)'''
s = [int(i)%k for i in input().strip().split()] 


remainder=[0]*k
ans=0
for i in s:
    remainder[i]+=1

for i in range(1,k//2):
    ans+=max(remainder[i],remainder[k-i])
if remainder[0]>0:
    ans+=1
if k%2==0 and remainder[k//2]>0:
    ans+=1
elif k%2==1 and k>1:
    ans+=max(remainder[k//2],remainder[k-k//2])
print(ans)
