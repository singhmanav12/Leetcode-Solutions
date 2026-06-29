class Solution(object):
    def longestPalindrome(self, s):
        n = len(s) 
        longest = ""
        
        if n <= 1:
            return s
            
        def CheckPalindrome(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
            
        for i in range(n):
            odd_s = CheckPalindrome(i, i)
            even_s = CheckPalindrome(i, i+1)
            if len(odd_s) > len(longest):
                longest = odd_s
                
            if len(even_s) > len(longest):
                longest = even_s
                
        return longest
