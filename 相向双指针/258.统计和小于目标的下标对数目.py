class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        n = len(nums)
        count = 0
        left,right = 0, n-1
        while left < right:
            # 排序后只要相加之和大于target，则右指针一直左移
            while right >= 0 and nums[left] + nums[right] >= target:
                right -= 1
            if left < right:
                count += right - left
            left += 1
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.countPairs([-1,1,2,3,1],2))