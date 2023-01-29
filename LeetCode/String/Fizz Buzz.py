#THIS IS MUCH BETTER THAN USING 'IF ELSE ELIF' AGAIN AND AGAIN
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list_of_output = [ 'Fizz' * (not i % 3) + 'Buzz' * (not i % 5 ) or str(i) for i in range(1, n+1) ]
        
        return list_of_output
