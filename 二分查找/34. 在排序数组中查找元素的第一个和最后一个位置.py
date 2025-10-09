"""由此纪念这是我第一次自己独立完成的最快的一道题"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            if nums[left] == nums[right] and nums[left] == target:
                return [left,right]
            if nums[left] < target:
                left += 1
            elif nums[right] > target:
                right -= 1
        
        return [-1,-1]