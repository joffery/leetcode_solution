class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        
        low = 0
        high = len(nums)
        mid = (low+high)/2
        
        while(low<mid):
            if nums[mid]<target:
                low = mid
                mid = (low+high)/2
            elif nums[mid]>target:
                high = mid
                mid = (low+high)/2
            else:
                return mid
        
        if target > nums[mid]:
            return high
        else:
            return low
                    