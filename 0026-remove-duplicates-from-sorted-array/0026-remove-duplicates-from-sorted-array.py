class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        j = 1
        k = 1
        while j < len(nums) :
            if nums[j] == nums[j-1] :
                j += 1
                continue
            else :
                nums[i+1] = nums[j]
                i += 1
                j += 1
                k += 1

        return k
