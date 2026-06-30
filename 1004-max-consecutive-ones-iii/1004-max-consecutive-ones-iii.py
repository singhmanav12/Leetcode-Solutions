class Solution(object):
    def longestOnes(self, nums, k):
        low = 0 
        res = 0 
        freq_0 = 0 
        for high in range(len(nums)) :
            if nums[high] == 0 :
                freq_0 += 1
            while freq_0 > k :
                if nums[low] == 0 :
                    freq_0 -= 1
                low += 1
            length = high - low + 1
            res = max(res, length)
        return res
        