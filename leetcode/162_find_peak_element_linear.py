class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums)-1
        for i in range(1,len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        return

# Didn't read prompt carefully for the ln n option