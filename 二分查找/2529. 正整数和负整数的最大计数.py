class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = neg = 0   #统计数目
        n = len(nums)
       
        left, right = 0 , n-1
        while left <= right:
            if nums[left] < 0:
                neg += 1
                left += 1
            if nums[right] > 0:
                right -= 1
                pos += 1
            if left <= right and nums[left] == 0:
                left += 1
            if left <= right and nums[right] == 0:
                right -= 1
        return pos if pos > neg else neg