class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        string = ""
        while columnNumber > 0:
            columnNumber -= 1
            string = chr(65 + columnNumber%26) + string
            columnNumber //= 26
        return string


'''
        ABCD = [(A)*26^3] + [(B)*26^2] + [(C)*26^1] + [(D)] 
        
        (A) = 1,(B) = 2 ......(AA) = 27....
        
        step1: ( n = n - 1 )
        
        step2: By n % 26 we get the columnuber of (alphabet)
        
        step3: Then we Add 65 (ord(A) == 65 ASCII) so that we can use it to get chr(columnuber) , 
                but if add 65 to (n % 26) ,then we get the next element , for eg :
                
                n = 701 then 701 % 26 = 25 --> chr(25+65) == Z , but we need Y (as columnuber = Y ) 
                therefore :
                we are n = n - 1 in step 1 ,
                n -> 700 , 700 % 26 = 24 --> chr(24+65) == Y
                
        step4: we divide it with 26 to jump to the next columnumber(B) (as it varies through 26^n) 
        
        step5 : repeat while n > 0 
        
        step 6 : return the reverse eg : we are jumping from A to D in (ABCD)
        
       '''
'''
	    n = 701
        n-1 = 700
        700 % 26 = 24
        res += chr(24+65) == Y
        n = 700 // 26 == 26
        
        n = 26
        n-1 = 25
        25 % 26 = 25 -> if a > b and a % b then (a % b = a) always
        res += chr(25+65) == Z
        n = 25 // 26 ==> 0
		
		'''
