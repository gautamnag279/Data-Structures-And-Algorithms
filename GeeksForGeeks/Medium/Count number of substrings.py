def substrCount(self, str, k):
    def getCount(str, k):
        char_count = [0]*26
        distinct_char = 0
    
        left = 0
        ans = 0
    
        for i in range(len(str)):
            curr_char = ord(str[i]) - ord('a')
            char_count[curr_char] += 1
    
            if char_count[curr_char] == 1:
                distinct_char += 1
            
            while distinct_char > k:
                curr_char = ord(str[left]) - ord('a')
                char_count[curr_char] -= 1
    
                if char_count[curr_char] == 0:
                    distinct_char -= 1
                
                left += 1
    
            ans += i - (left + 1)
    
        return ans 
    
    return getCount(str, k) - getCount(str, k-1)