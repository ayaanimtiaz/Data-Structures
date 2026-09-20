class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
       # find minimum
       # use as pivot
       # check ranges


        left = 0
        right = len(nums) -1
        middle = (left + right) // 2

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        
        min_pivot = left

        l = 0
        r = len(nums) - 1
        m = (r + l) // 2

        if min_pivot == 0:
            l = 0
            r = len(nums) - 1
        elif nums[l] <= target and target <= nums[min_pivot - 1]:
            r = min_pivot - 1
        elif nums[min_pivot] <= target and target <= nums[r]:
            l = min_pivot 
        
        while l <= r:
            m = (r+l) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        

        return -1


        
        



            