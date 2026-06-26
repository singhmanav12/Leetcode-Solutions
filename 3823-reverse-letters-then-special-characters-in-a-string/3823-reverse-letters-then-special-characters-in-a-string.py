class Solution(object):
    def reverseByType(self, s):
        n=len(s)-1
        left = 0
        right = n
        a = list(s)
        while left < right:
            while left < right and  not a[left].isalpha():
                left+=1
            while left < right and not a[right].isalpha():
                right-=1
            
            a[left], a[right] = a[right], a[left]
            left+=1
            right-=1
        left = 0
        right = n
        while left < right:
            while left < right and a[left].isalpha():
                left+=1
            while left < right and a[right].isalpha():
                right-=1
            
            a[left], a[right] = a[right], a[left]
            left+=1
            right-=1
        return "".join(a)