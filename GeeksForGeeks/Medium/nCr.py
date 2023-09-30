def nCr(self, n, r):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result
    
    if r > n:
        return 0
    else:
        ans = (factorial(n))//(factorial(r)*(factorial(n-r)))
        return ans%(1000000007)