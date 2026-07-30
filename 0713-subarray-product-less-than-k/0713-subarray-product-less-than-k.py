class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        # Edge case: Since all numbers are positive integers (min 1), 
        # a product can never be strictly less than 0 or 1.
        if k <= 1:
            return 0
        
        product = 1
        count = 0
        left = 0
        
        # Expand the window by moving the right pointer
        for right in range(len(nums)):
            product *= nums[right]
            
            # Shrink the window from the left if the product is too large
            while product >= k:
                product /= nums[left]
                left += 1
                
            # Add the number of valid subarrays ending at the current 'right' position
            count += right - left + 1
            
        return count


