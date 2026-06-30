class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        current_1 = 0 
        max_1 = 0 
        for i in range(len(nums)) :
            if nums[i] == 1 :
                current_1 += 1
                max_1 = max(max_1, current_1)
            else :
                current_1 = 0
            
        return max_1

            
