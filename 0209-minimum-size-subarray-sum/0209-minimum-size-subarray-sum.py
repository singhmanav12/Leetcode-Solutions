class Solution(object):
    def minSubArrayLen(self, target, nums):
        low =0
        sum = 0
        res = float('inf')
        for high in range(len(nums)):
            sum += nums[high]
            while sum >= target :
                length = high - low +1 
                res = min(res,length)
                sum -= nums[low]
                low += 1
        if res == float('inf') :
            return 0
        else :
            return res

    