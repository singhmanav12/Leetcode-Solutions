class Solution(object):
    def validPalindrome(self, s):
        def Check_Palin(s,i,j) :
            while i < j :
                if s[i] != s[j] :
                    return False
                else :
                    i += 1
                    j -=1
            return True
        left =0
        right=len(s)-1
        while left < right :
            if s[left] != s[right] :
                delete_left = Check_Palin(s,left+1,right)
                delete_right = Check_Palin(s,left,right-1)
                return delete_left or delete_right

            else :
                left += 1
                right -=1
        return True