class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        i=0
        for i in range(len(nums)-2) :
            if i>0 and nums[i]==nums[i-1] :
                continue 
            else :
                left = i+1
                right = len(nums)-1
                sum = -1*nums[i]
                while left < right :
                    if nums[left] + nums[right] == sum :
                        result.append([nums[i],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left < len(nums)-1 and nums[left]==nums[left-1] :
                            left+=1
                        while right >=0 and nums[right]==nums[right+1] :
                            right-=1
                    elif nums[left] + nums[right] < sum :
                        left+=1
                    else :
                        right-=1
        return result